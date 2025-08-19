#!/usr/bin/env python3
"""Setup script for the project template."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command."""
    print(f"Running: {cmd}")
    return subprocess.run(cmd, shell=True, check=check)


def main() -> None:
    """Set up the development environment."""
    print("🚀 개발 환경 설정을 시작합니다...")

    # 프로젝트 초기화 스크립트가 있는지 확인
    initialize_script = Path(__file__).parent / "initialize_project.py"
    if initialize_script.exists():
        print("\n📌 새 프로젝트 설정이 필요한 것 같습니다!")
        use_template = (
            input("이 템플릿을 사용해서 새 프로젝트를 만드시겠습니까? [y/N]: ")
            .strip()
            .lower()
        )
        if use_template in ["y", "yes"]:
            print("프로젝트 초기화 스크립트를 실행합니다...")
            run_command("python scripts/initialize_project.py")
            return

    # Check if uv is installed
    try:
        run_command("uv --version")
    except subprocess.CalledProcessError:
        print("❌ uv가 설치되어 있지 않습니다. 먼저 설치해주세요:")
        print("curl -LsSf https://astral.sh/uv/install.sh | sh")
        sys.exit(1)

    # Install dependencies
    print("\n1. 의존성 설치 중...")
    run_command("uv sync --dev")

    # Set up pre-commit hooks
    print("\n2. pre-commit 훅 설정 중...")
    run_command("uv run pre-commit install")

    # Run initial code quality checks
    print("\n3. 코드 품질 검사 실행 중...")
    run_command("uv run pre-commit run --all-files", check=False)

    # Run tests
    print("\n4. 테스트 실행 중...")
    run_command("uv run pytest")

    print("\n✅ 설정 완료! 개발을 시작할 수 있습니다.")
    print("\n💡 유용한 명령어들:")
    print("  uv run pytest          # 테스트 실행")
    print("  uv run black .         # 코드 포맷팅")
    print("  uv run flake8 .        # 린팅")
    print("  uv run mypy src        # 타입 체킹")
    print("  uv add <package>       # 의존성 추가")
    print("  uv add --dev <package> # 개발 의존성 추가")


if __name__ == "__main__":
    main()
