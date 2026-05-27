# Module Convention

## 네이밍

- 폴더명: `번호-기능명`
- 패키지명: 숫자를 제거하고 `snake_case`로 변환
- 예시: `16-3d-reconstruction-helper` -> `three_d_reconstruction_helper`

## 기본 구조

모든 모듈은 아래 항목을 포함합니다.

- `README.md`
- `pyproject.toml`
- `.env.example`
- `run.py`
- `data/input/.gitkeep`
- `data/output/.gitkeep`
- `notebooks/.gitkeep`
- `src/<package_name>/`
- `tests/test_basic.py`

## 구현 원칙

- 공통 유틸은 `shared/`에 둡니다.
- 실제 모델 다운로드 코드는 기본 골격에 넣지 않습니다.
- 테스트는 최소 동작을 검증하는 수준부터 시작합니다.
- 모듈별 의존성은 필요한 시점에만 추가합니다.
