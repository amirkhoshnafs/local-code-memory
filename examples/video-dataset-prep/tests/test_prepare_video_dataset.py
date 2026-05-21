from pathlib import Path

import cv2
import numpy as np

from src.prepare_video_dataset import extract_frames, find_video_files


def create_test_video(video_path: Path, num_frames: int = 12) -> None:
    writer = cv2.VideoWriter(
        str(video_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        10,
        (64, 64),
    )

    for i in range(num_frames):
        frame = np.zeros((64, 64, 3), dtype=np.uint8)
        frame[:, :] = (0, 0, min(i * 20, 255))
        writer.write(frame)

    writer.release()


def test_extract_frames_with_none_max_frames(tmp_path):
    video_path = tmp_path / "sample.mp4"
    output_dir = tmp_path / "dataset" / "images"

    create_test_video(video_path, num_frames=10)

    saved_count = extract_frames(
        video_path=video_path,
        output_dir=output_dir,
        stride=2,
        max_frames_per_video=None,
    )

    saved_images = sorted(output_dir.glob("*.jpg"))

    assert saved_count == 5
    assert len(saved_images) == 5


def test_extract_frames_respects_max_frames(tmp_path):
    video_path = tmp_path / "sample.mp4"
    output_dir = tmp_path / "dataset" / "images"

    create_test_video(video_path, num_frames=20)

    saved_count = extract_frames(
        video_path=video_path,
        output_dir=output_dir,
        stride=2,
        max_frames_per_video=3,
    )

    saved_images = sorted(output_dir.glob("*.jpg"))

    assert saved_count == 3
    assert len(saved_images) == 3


def test_find_supported_video_files(tmp_path):
    videos_dir = tmp_path / "videos"
    videos_dir.mkdir()

    supported = [
        videos_dir / "a.mp4",
        videos_dir / "b.avi",
        videos_dir / "c.mov",
        videos_dir / "d.mkv",
    ]

    unsupported = [
        videos_dir / "notes.txt",
        videos_dir / "image.jpg",
    ]

    for path in supported + unsupported:
        path.write_text("dummy")

    found = find_video_files(videos_dir)
    found_names = [path.name for path in found]

    assert found_names == ["a.mp4", "b.avi", "c.mov", "d.mkv"]
