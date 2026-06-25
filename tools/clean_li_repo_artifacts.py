#!/usr/bin/env python3
from pathlib import Path

for path in Path(".").rglob("__pycache__"):
    if path.is_dir():
        for child in path.rglob("*"):
            if child.is_file():
                child.unlink()
        try:
            path.rmdir()
        except OSError:
            pass
print("Repo hygiene clean.")
