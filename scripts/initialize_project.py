#!/usr/bin/env python3
"""프로젝트 초기화 스크립트

이 스크립트는 템플릿에서 새 프로젝트를 생성할 때 사용됩니다.
프로젝트 메타데이터를 새 프로젝트 이름으로 업데이트하고,
실행 후 자동으로 삭제됩니다.
"""

import re
import sys
from pathlib import Path


def get_project_name() -> str:
    """사용자로부터 프로젝트 이름을 입력받습니다."""
    while True:
        name = input("새 프로젝트 이름을 입력하세요 (예: my-awesome-project): ").strip()
        if name and re.match(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]$", name):
            return name
        print("유효하지 않은 프로젝트 이름입니다. 소문자, 숫자, 하이픈만 사용하세요.")


def get_package_name(project_name: str) -> str:
    """프로젝트 이름에서 패키지 이름을 생성합니다."""
    return project_name.replace("-", "_")


def get_user_info() -> tuple[str, str]:
    """사용자 정보를 입력받습니다."""
    author_name = input("작성자 이름을 입력하세요: ").strip()
    author_email = input("작성자 이메일을 입력하세요: ").strip()
    return author_name, author_email


def get_github_info(project_name: str) -> str:
    """GitHub 사용자명을 입력받습니다."""
    github_username = input("GitHub 사용자명을 입력하세요: ").strip()
    return github_username


def update_pyproject_toml(
    project_root: Path,
    project_name: str,
    package_name: str,
    author_name: str,
    author_email: str,
    github_username: str,
) -> None:
    """pyproject.toml 파일을 업데이트합니다."""
    pyproject_path = project_root / "pyproject.toml"
    content = pyproject_path.read_text(encoding="utf-8")

    # 프로젝트 이름 및 메타데이터 업데이트
    content = content.replace(
        'name = "python-project-template"', f'name = "{project_name}"'
    )
    content = content.replace(
        'description = "A modern Python project template using uv package manager"',
        'description = "Add your description here"',
    )
    content = content.replace(
        '{ name = "Your Name", email = "your.email@example.com" }',
        f'{{ name = "{author_name}", email = "{author_email}" }}',
    )

    # GitHub URL 업데이트
    content = content.replace(
        "your-username/python-project-template", f"{github_username}/{project_name}"
    )
    content = content.replace(
        'my-project = "src.main:main"', f'{package_name} = "src.main:main"'
    )

    pyproject_path.write_text(content, encoding="utf-8")
    print(f"✅ {pyproject_path} 업데이트 완료")


def update_readme(project_root: Path, project_name: str, github_username: str) -> None:
    """README.md 파일을 업데이트합니다."""
    readme_path = project_root / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    # 프로젝트 이름과 URL 업데이트
    content = content.replace(
        "Python Project Template", project_name.replace("-", " ").title()
    )
    content = content.replace("python-project-template", project_name)
    content = content.replace("your-username", github_username)

    # 템플릿 관련 설명 제거하고 기본 설명으로 변경
    lines = content.split("\n")
    new_lines = []
    skip_section = False

    for line in lines:
        if line.startswith("현대적인 Python 프로젝트를 위한 템플릿입니다"):
            new_lines.append("Python 프로젝트 설명을 여기에 작성하세요.")
            continue
        elif line.startswith("### 1. 템플릿 사용"):
            skip_section = True
            continue
        elif line.startswith("### 2. 로컬 설정"):
            skip_section = False
            new_lines.append("### 설치 및 설정")
            continue
        elif not skip_section:
            new_lines.append(line)

    readme_path.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"✅ {readme_path} 업데이트 완료")


def update_license(project_root: Path, author_name: str) -> None:
    """LICENSE 파일을 업데이트합니다."""
    license_path = project_root / "LICENSE"
    content = license_path.read_text(encoding="utf-8")

    import datetime

    current_year = datetime.datetime.now().year

    content = content.replace(
        "Copyright (c) 2024 [Your Name]", f"Copyright (c) {current_year} {author_name}"
    )

    license_path.write_text(content, encoding="utf-8")
    print(f"✅ {license_path} 업데이트 완료")


def update_init_file(project_root: Path, project_name: str) -> None:
    """src/__init__.py 파일을 업데이트합니다."""
    init_path = project_root / "src" / "__init__.py"
    content = init_path.read_text(encoding="utf-8")

    project_title = project_name.replace("-", " ").title()
    content = content.replace("Python Project Template", project_title)
    content = content.replace(
        "A template for Python projects using uv package manager.",
        "Add your project description here.",
    )

    init_path.write_text(content, encoding="utf-8")
    print(f"✅ {init_path} 업데이트 완료")


def cleanup_template_files(project_root: Path) -> None:
    """템플릿 관련 파일들을 정리합니다."""
    # CONTRIBUTING.md 파일 제거 (새 프로젝트에서는 필요 없음)
    contributing_path = project_root / "CONTRIBUTING.md"
    if contributing_path.exists():
        contributing_path.unlink()
        print(f"✅ {contributing_path} 제거 완료")

    # 이 스크립트 자체를 제거
    script_path = project_root / "scripts" / "initialize_project.py"
    if script_path.exists():
        script_path.unlink()
        print(f"✅ {script_path} 제거 완료")


def main() -> None:
    """메인 함수"""
    print("🚀 Python 프로젝트 템플릿 초기화")
    print("=" * 50)

    # 프로젝트 루트 디렉토리 확인
    project_root = Path(__file__).parent.parent

    try:
        # 사용자 입력 받기
        project_name = get_project_name()
        package_name = get_package_name(project_name)
        author_name, author_email = get_user_info()
        github_username = get_github_info(project_name)

        print("\n📋 프로젝트 정보:")
        print(f"   - 프로젝트 이름: {project_name}")
        print(f"   - 패키지 이름: {package_name}")
        print(f"   - 작성자: {author_name} <{author_email}>")
        print(f"   - GitHub: {github_username}/{project_name}")

        # 확인
        confirm = input("\n계속 진행하시겠습니까? [y/N]: ").strip().lower()
        if confirm not in ["y", "yes"]:
            print("취소되었습니다.")
            return

        print("\n🔄 프로젝트 파일들을 업데이트하는 중...")

        # 파일들 업데이트
        update_pyproject_toml(
            project_root,
            project_name,
            package_name,
            author_name,
            author_email,
            github_username,
        )
        update_readme(project_root, project_name, github_username)
        update_license(project_root, author_name)
        update_init_file(project_root, project_name)

        # 템플릿 파일들 정리
        cleanup_template_files(project_root)

        print(f"\n✅ 프로젝트 '{project_name}' 초기화가 완료되었습니다!")
        print("\n📌 다음 단계:")
        print("   1. uv sync --dev  # 의존성 설치")
        print("   2. uv run pre-commit install  # pre-commit 훅 설정")
        print("   3. uv run pytest  # 테스트 실행")
        print("   4. git add . && git commit -m 'Initial commit'  # 첫 커밋")

    except KeyboardInterrupt:
        print("\n\n취소되었습니다.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
