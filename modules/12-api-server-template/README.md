# 12-api-server-template

## 목적

Python API 서버를 빠르게 시작하기 위한 최소 템플릿입니다.

## 주요 기능

- 엔드포인트 추가를 고려한 기본 패키지 구조
- 추후 설정, 라우터, 미들웨어 분리를 쉽게 만드는 시작점
- 간단한 실행 결과 딕셔너리 반환 예시

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

HTTP 요청, 환경변수 기반 설정, 서비스 옵션

## Output

응답 데이터, 상태 메시지, 서버 메타정보

## Example Output

```python
{
  "module": "12-api-server-template",
  "package": "api_server_template",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 웹 프레임워크 연결
- 헬스체크와 기본 라우터 추가
