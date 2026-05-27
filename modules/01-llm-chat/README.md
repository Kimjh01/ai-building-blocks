# 01-llm-chat

## 목적

대화형 LLM 기능을 빠르게 붙일 수 있는 최소 실행 골격을 제공합니다.

## 주요 기능

- 시스템 프롬프트와 사용자 입력 흐름 시작점
- 모델 호출 로직을 붙이기 쉬운 `main()` 엔트리포인트
- 향후 대화 이력 관리와 툴 호출을 확장하기 위한 기본 구조

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

사용자 질문 텍스트, 시스템 프롬프트, API 키 같은 환경변수 설정

## Output

모델 응답, 실행 상태, 메타데이터를 담는 결과 딕셔너리

## Example Output

```python
{
  "module": "01-llm-chat",
  "package": "llm_chat",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 LLM API 호출 로직 추가
- 대화 히스토리 저장 구조 추가
