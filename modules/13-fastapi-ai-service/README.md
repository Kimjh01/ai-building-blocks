# 13-fastapi-ai-service

## 목적

FastAPI 기반 AI 서비스 실험을 위한 시작 구조입니다.

## 주요 기능

- AI 추론 로직과 API 계층을 분리하기 쉬운 구조
- 입력 검증과 응답 모델 확장을 고려한 엔트리포인트
- 서비스 결과를 공통 딕셔너리로 반환

## Setup

```bash
uv venv
uv pip install -e ../../shared
uv pip install -e .
```

## Run

```bash
python run.py
```

## Input

API 요청 바디, 모델 설정, 서비스 환경변수

## Output

추론 결과, 응답 메타정보, 상태 정보

## Example Output

```python
{
  "module": "13-fastapi-ai-service",
  "package": "fastapi_ai_service",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- FastAPI 앱과 라우터 추가
- 요청/응답 스키마 세분화
