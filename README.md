# bnbong.xyz

bnbong.xyz 메인 허브 프로젝트

- `bnbong.xyz` : bnbong의 개인 포트폴리오 사이트
- `playground.bnbong.xyz` : bnbong이 개발한 웹 게임 모음 플랫폼
- `api.bnbong.xyz` : bnbong이 개발한 backend API 게이트웨이, Bifrost (하위 API 서버 프록시)

## Architecture

```bash
bnbong/
│── docker-compose.yml          # 전체 서비스 오케스트레이션
│── .gitignore
│── .pre-commit-config.yaml
│── .yamllint
│── .github/
│── README.md
│── DEPLOYMENT.md              # 배포 가이드
│
├── gateway/                   # API Gateway, Bifrost (FastAPI)
│   ├── src/
│   │   ├── main.py           # 메인 애플리케이션
│   │   ├── config.py         # 설정 관리
│   │   └── core/
│   │       ├── middleware.py # 미들웨어 (로깅, 레이트 리미팅)
│   │       ├── router.py     # API 라우터
│   │       └── services.py   # 서비스 레지스트리 및 프록시
│   ├── Dockerfile
│   └── requirements.txt
│
├── auth-server/               # JWT Auth server (FastAPI)
│   ├── src/
│   │   ├── main.py           # 메인 애플리케이션
│   │   ├── config.py         # 설정 관리
│   │   ├── core/
│   │   │   ├── auth.py       # 인증 라우터
│   │   │   ├── users.py      # 사용자 관리
│   │   │   └── database.py   # 데이터베이스 설정
│   │   └── models/
│   │       └── user.py       # 사용자 모델
│   ├── Dockerfile
│   └── requirements.txt
│
├── client/                    # Web Client (React, Portfolio + Admin Panel)
│   ├── package.json          # React + TypeScript + Vite
│   ├── Dockerfile
│   └── nginx.conf
│
├── playground/                # Game Collection Platform (React)
│   ├── package.json          # React + TypeScript + Vite
│   ├── Dockerfile
│   └── nginx.conf
│
├── nginx/                     # Reverse Proxy 설정
│   ├── nginx.conf            # 도메인별 라우팅 설정
│   └── ssl/                  # SSL 인증서 디렉토리
│
└── infra/                     # Terraform IaC
    ├── main.tf               # 메인 인프라 설정
    ├── variables.tf          # 변수 정의
    ├── user_data.sh          # 인스턴스 초기화 스크립트
    └── terraform.tfvars.example
```

## Stack

- **Cloud**: OCI + Terraform IaC
- **Deployment**: Docker Compose
- **API Gateway (Bifrost)**: FastAPI + Python 3.12+
- **Auth Server**: FastAPI + Python 3.12+ + JWT + PostgreSQL
- **Client (Portfolio + Admin)**: React + TypeScript + Vite + Tailwind CSS
- **Playground**: React + TypeScript + Vite + Framer Motion
- **Database**: PostgreSQL + Redis
- **Reverse Proxy**: Nginx
- **SSL**: Cloudflare (자동 SSL 인증서 관리)
- **CI/CD**: GitHub Actions (예정)
- **Monitoring**: Prometheus + Grafana (예정)

## 주요 기능

### API Gateway (Bifrost)
- ✅ 동적 서비스 라우팅
- ✅ 요청/응답 로깅
- ✅ 레이트 리미팅
- ✅ 헬스 체크
- ✅ 관리자 API (서비스 등록/제거)

### Auth Server
- ✅ JWT 기반 인증
- ✅ 사용자 등록/로그인
- ✅ 토큰 갱신
- ✅ API 키 관리
- ✅ 슈퍼유저 권한 관리

### Client (Portfolio + Admin)
- ✅ 포트폴리오 사이트
- ✅ 관리자 패널 (예정)
- ✅ 반응형 디자인
- ✅ SEO 최적화

### Playground
- ✅ 게임 컬렉션 플랫폼
- ✅ 사용자 인증
- ✅ 게임 점수 관리 (예정)
- ✅ 실시간 게임 (예정)

## 빠른 시작

### 1. 로컬 개발 환경

#### UV를 사용한 개발 (권장)

```bash
# 저장소 클론
git clone https://github.com/bnbong/bnbong.xyz.git
cd bnbong.xyz

# Gateway 서비스 설정
cd gateway
uv sync
cp env.example .env  # 환경 변수 설정
./dev.sh  # 개발 서버 실행

# Auth Server 설정 (새 터미널에서)
cd ../auth-server
uv sync
cp env.example .env  # 환경 변수 설정
./dev.sh  # 개발 서버 실행
```

#### Docker를 사용한 개발

```bash
# 저장소 클론
git clone https://github.com/bnbong/bnbong.xyz.git
cd bnbong.xyz

# 환경 변수 설정
cp env.example .env
# .env 파일 편집

# 서비스 시작
docker-compose up -d

# 서비스 확인
docker-compose ps
```

### 2. 프로덕션 배포

자세한 배포 가이드는 [DEPLOYMENT.md](./DEPLOYMENT.md)를 참조하세요.

```bash
# 1. 인프라 배포
cd infra
terraform init
terraform apply

# 2. 애플리케이션 배포 (자동화된 스크립트 사용)
chmod +x infra/deploy.sh
./infra/deploy.sh [서버_IP] ubuntu

# 또는 수동 배포
rsync -avz --exclude='.git' --exclude='node_modules' . ubuntu@[서버_IP]:/opt/bnbong/
ssh ubuntu@[서버_IP] 'cd /opt/bnbong && docker-compose up -d --build'
```

## API 엔드포인트

### API Gateway (api.bnbong.xyz)
- `GET /health` - 헬스 체크
- `GET /services` - 등록된 서비스 목록
- `GET /services/{service_name}/health` - 서비스 헬스 체크
- `/{service_name}/{path}` - 서비스 프록시

### Auth Server
- `POST /auth/token` - 로그인
- `POST /auth/refresh` - 토큰 갱신
- `GET /auth/me` - 현재 사용자 정보
- `POST /users/register` - 사용자 등록

## 개발 가이드

- [UV 패키지 매니저 사용법](./UV_GUIDE.md) - FastAPI 서비스 개발 환경 설정
- [배포 가이드](./DEPLOYMENT.md) - 프로덕션 배포 방법

## 개발 로드맵

### Phase 1: 기본 인프라 ✅
- [x] 프로젝트 구조 설계
- [x] Docker Compose 설정
- [x] Terraform 인프라 코드
- [x] API Gateway 구현
- [x] Auth Server 구현

### Phase 2: 프론트엔드 개발 🔄
- [ ] React 클라이언트 구현
- [ ] 포트폴리오 사이트
- [ ] 관리자 패널
- [ ] Playground 플랫폼

### Phase 3: 게임 통합 🔄
- [ ] Pygame 웹 변환
- [ ] 게임 실행 엔진
- [ ] 점수 시스템
- [ ] 리더보드

### Phase 4: 고급 기능 📋
- [ ] 모니터링 시스템
- [ ] CI/CD 파이프라인
- [ ] 백업 시스템
- [ ] 성능 최적화
