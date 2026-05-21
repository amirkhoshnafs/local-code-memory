import argparse
import logging
from pathlib import Path

import cv2

logging.basicConfig(level=logging.INFO)

VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv"}


def find_video_files(videos_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in videos_dir.iterdir()
        if path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS
    )


def extract_frames(
    video_path: Path,
    output_dir: Path,
    stride: int,
    max_frames_per_video: int | None,
) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        logging.error("Could not open video file: %s", video_path)
        return 0

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % stride == 0:
            if max_frames_per_video is not None and saved_frame_count >= max_frames_per_video:
                break

            output_path = output_dir / f"{video_path.stem}_frame_{saved_frame_count:06d}.jpg"
            cv2.imwrite(str(output_path), frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    logging.info("Extracted %s frames from %s", saved_frame_count, video_path)
    return saved_frame_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare an image dataset from videos")
    parser.add_argument("--videos-dir", type=Path, required=True, help="Directory containing video files")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output dataset directory")
    parser.add_argument("--stride", type=int, default=10, help="Extract one frame every N frames")
    parser.add_argument("--max-frames-per-video", type=int, default=None, help="Optional frame cap per video")

    args = parser.parse_args()

    images_dir = args.output_dir / "images"
    total_saved_frames = 0

    for video_path in find_video_files(args.videos_dir):
        total_saved_frames += extract_frames(
            video_path=video_path,
            output_dir=images_dir,
            stride=args.stride,
            max_frames_per_video=args.max_frames_per_video,
        )

    print(f"Videos found: {len(find_video_files(args.videos_dir))}")
    print(f"Frames saved: {total_saved_frames}")
    print(f"Images directory: {images_dir}")


if __name__ == "__main__":
    main()
