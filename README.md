# Python Project Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

현대적인 Python 프로젝트를 위한 템플릿입니다. `uv` 패키지 매니저를 사용하여 개발 도구, 테스팅, CI/CD 워크플로우가 사전 구성되어 있습니다.

## 🚀 빠른 시작

### 1. 템플릿 사용

이 템플릿으로 새 저장소를 만들려면:

1. GitHub에서 "Use this template" 버튼 클릭
2. 새 저장소 이름 입력
3. 저장소 생성

### 2. 로컬 설정

```bash
# 저장소 클론
git clone https://github.com/your-username/your-project-name.git
cd your-project-name

# uv 설치 (이미 설치되어 있다면 생략)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 프로젝트 초기화 및 설정 (새 프로젝트인 경우)
python scripts/setup.py
```

새 프로젝트를 만들 때는 자동으로 프로젝트 초기화 스크립트가 실행되어 프로젝트 이름, 작성자 정보 등을 설정할 수 있습니다.

기존 프로젝트 개발을 계속하는 경우:

```bash
# 의존성 설치
uv sync --dev

# pre-commit 훅 설정
uv run pre-commit install

# 테스트 실행
uv run pytest
```

## 📁 프로젝트 구조

```
your-project/
├── src/                    # 소스 코드
│   └── __init__.py
├── tests/                  # 테스트 파일
│   └── __init__.py
├── .github/
│   └── workflows/          # GitHub Actions
│       ├── ci.yml          # CI 파이프라인 (버전 별 테스트 및 린팅)
│       └── release.yml     # 패키지 빌드
├── scripts/                # 유틸리티 스크립트
│   ├── setup.py           # 개발 환경 설정
│   ├── clean.py           # 빌드 아티팩트 정리
│   └── initialize_project.py # 프로젝트 초기화 (템플릿용)
├── .gitignore             # Git 무시 파일
├── .pre-commit-config.yaml # Pre-commit 설정
├── LICENSE                # MIT 라이선스
├── README.md              # 프로젝트 설명
├── pyproject.toml         # 프로젝트 설정
└── uv.lock               # 의존성 잠금 파일
```

## 🔧 개발

### 의존성 관리

```bash
# 런타임 의존성 추가
uv add requests

# 개발 의존성 추가
uv add --dev pytest-mock

# 의존성 제거
uv remove requests
```

### 코드 품질 도구

```bash
# 코드 포맷팅
uv run black .

# import 정렬
uv run isort .

# 린팅
uv run flake8 .

# 타입 체킹
uv run mypy src

# 모든 품질 검사 실행
uv run pre-commit run --all-files
```

### 테스팅

```bash
# 모든 테스트 실행
uv run pytest

# 커버리지 포함 테스트
uv run pytest --cov=src

# 특정 테스트 파일 실행
uv run pytest tests/test_main.py

# 특정 마커를 가진 테스트 실행
uv run pytest -m "not slow"
```

### 프로젝트 정리

```bash
# 캐시 및 빌드 아티팩트 정리
python scripts/clean.py
```

## 📦 빌드 및 배포

### 패키지 빌드

```bash
uv build
```

### PyPI 배포

```bash
# 수동 배포
uv publish

# 또는 GitHub Actions 사용 (태그 푸시 시 자동)
git tag v0.1.0
git push origin v0.1.0
```

## ⚡ GitHub Actions

템플릿에는 두 가지 워크플로우가 포함되어 있습니다:

1. **CI** (`.github/workflows/ci.yml`): 테스트, 린팅, 타입 체킹
2. **릴리스** (`.github/workflows/release.yml`): 태그 푸시 시 자동 패키지 배포 (PyPI 수동 등록 필요)

## 🛠️ 사용자 정의

### 프로젝트 정보 업데이트

1. `pyproject.toml`에서 프로젝트 메타데이터 수정:
   - `name`: 프로젝트 이름
   - `description`: 프로젝트 설명
   - `authors`: 작성자 정보
   - `urls`: 저장소 URL

2. `LICENSE` 파일에서 저작권 정보 수정

3. 이 `README.md`에서 배지와 URL 업데이트

### 추가 도구 구성

필요에 따라 다음을 추가할 수 있습니다:

- **Ruff**: 더 빠른 린터/포매터
- **Docker**: 컨테이너화
- **Makefile**: 빌드 자동화

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 지원

문제가 있거나 질문이 있으시면 [이슈](https://github.com/your-username/python-project-template/issues)를 생성해 주세요.
