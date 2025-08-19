#!/usr/bin/env python3
"""Clean up build artifacts and cache files."""

import shutil
from pathlib import Path


def remove_patterns(root: Path, patterns: list[str]) -> None:
    """Remove files and directories matching the given patterns."""
    for pattern in patterns:
        for path in root.rglob(pattern):
            if path.exists():
                if path.is_file():
                    print(f"Removing file: {path}")
                    path.unlink()
                elif path.is_dir():
                    print(f"Removing directory: {path}")
                    shutil.rmtree(path)


def main() -> None:
    """Clean up the project directory."""
    root = Path(__file__).parent.parent

    print("🧹 프로젝트 디렉토리 정리 중...")

    # Cache and build artifacts
    cache_patterns = [
        "__pycache__",
        "*.pyc",
        "*.pyo",
        "*.egg-info",
        ".pytest_cache",
        ".coverage",
        "htmlcov",
        ".mypy_cache",
        ".tox",
        "build",
        "dist",
        ".eggs",
    ]

    remove_patterns(root, cache_patterns)

    print("✅ 정리 완료!")


if __name__ == "__main__":
    main()
