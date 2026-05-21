#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="$HOME/.local/bin"

mkdir -p "$BIN_DIR"

cp "$ROOT_DIR/scripts/code-memory" "$BIN_DIR/code-memory"
chmod +x "$BIN_DIR/code-memory"

echo "Installed: $BIN_DIR/code-memory"

case ":$PATH:" in
  *":$BIN_DIR:"*)
    echo "OK: $BIN_DIR is already in PATH"
    ;;
  *)
    echo "WARNING: $BIN_DIR is not in PATH."
    echo
    echo "Add this to your shell config:"
    echo "export PATH=\"$BIN_DIR:\$PATH\""
    echo
    echo "For fish:"
    echo "fish_add_path -m $BIN_DIR"
    ;;
esac

echo
echo "Try it:"
echo "  cd /path/to/project"
echo "  code-memory ."
