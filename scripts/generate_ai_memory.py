#!/usr/bin/env python3
"""Compatibility helper. Prefer scripts/code-memory."""
from pathlib import Path
import subprocess
import sys

script = Path(__file__).resolve().parent / "code-memory"
project = sys.argv[1] if len(sys.argv) > 1 else "."
raise SystemExit(subprocess.call([str(script), project]))
