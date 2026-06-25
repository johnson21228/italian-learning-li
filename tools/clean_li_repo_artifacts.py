#!/usr/bin/env python3
"""Clean generated LI/workbench artifacts before packing.

Preserves the canonical LLM continuity snapshot:
outputs/history/repo_history_for_llm.md

Removes legacy timestamped repo_history_for_llm_*.md files so repeated pack
runs do not create history clutter.
"""
from pathlib import Path
import shutil

ROOT = Path('.')

REMOVE_DIR_NAMES = {
    'overlay',
    'files',
    '__MACOSX',
}

REMOVE_DIR_GLOBS = [
    '*_overlay',
    '*_overlay_v*',
]

REMOVE_FILE_GLOBS = [
    'apply_*_overlay.py',
    'apply_*_overlay_*.py',
    '*_overlay.zip',
    '*_overlay_v*.zip',
    '.DS_Store',
    '**/.DS_Store',
]


def remove_dir(path: Path) -> None:
    if path.exists() and path.is_dir():
        shutil.rmtree(path)
        print(f'Removed directory {path}')


def remove_file(path: Path) -> None:
    if path.exists() and path.is_file():
        path.unlink()
        print(f'Removed file {path}')


for name in sorted(REMOVE_DIR_NAMES):
    remove_dir(ROOT / name)

for pattern in REMOVE_DIR_GLOBS:
    for path in sorted(ROOT.glob(pattern)):
        if path.is_dir() and path.name not in {'.git', 'dist', 'outputs'}:
            remove_dir(path)

for pattern in REMOVE_FILE_GLOBS:
    for path in sorted(ROOT.glob(pattern)):
        remove_file(path)

history_dir = ROOT / 'outputs' / 'history'
if history_dir.exists():
    canonical = history_dir / 'repo_history_for_llm.md'
    for old in sorted(history_dir.glob('repo_history_for_llm_*.md')):
        if old != canonical:
            old.unlink()
            print(f'Removed legacy timestamped history {old}')

print('LI cleanup complete.')
