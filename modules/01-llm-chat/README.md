# 01-llm-chat

## 목적

OpenAI 호환 Chat Completions API를 기준으로 가장 먼저 재사용하게 되는 LLM 채팅 기능의 최소 구현을 제공합니다. API 키가 없을 때도 `dry-run`으로 즉시 실행되도록 만들어 초기 연결 테스트에 바로 쓸 수 있습니다.

## 주요 기능

- `python run.py --message "..."` 형태의 간단한 CLI 실행
- `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL` 기반 설정
- API 키가 없으면 자동으로 `dry-run` 응답 반환
- 대화 히스토리를 `data/output/chat_history.json`에 저장
- 마지막 실행 결과를 `data/output/last_response.json`에 저장

## Setup

```bash
uv venv
uv pip install -e ../../shared
uv pip install -e .
```

`.env.example`를 참고해서 필요하면 `.env`를 만듭니다.

## Run

기본 실행:

```bash
python run.py
```

메시지를 직접 넘기는 실행:

```bash
python run.py --message "RAG 챗봇의 기본 구조를 설명해줘"
```

강제로 드라이런:

```bash
python run.py --message "테스트" --dry-run
```

히스토리 없이 단발 실행:

```bash
python run.py --message "한 번만 실행" --no-save-history --reset-history
```

## Input

- 사용자 메시지
- 시스템 프롬프트
- `.env`의 OpenAI 호환 API 설정
- 기존 대화 히스토리 파일

## Output

- 실행 결과 딕셔너리
- `data/output/chat_history.json`
- `data/output/last_response.json`

## Example Output

```python
{
  "module": "01-llm-chat",
  "package": "llm_chat",
  "status": "ok",
  "dry_run": True,
  "assistant": {
    "role": "assistant",
    "content": "[dry-run] API 키가 없어 실제 호출 대신 입력만 확인했습니다: 테스트"
  }
}
```

## TODO

- 스트리밍 응답 지원
- 멀티턴 요약 메모리 추가
- 툴 호출과 함수 실행 인터페이스 추가
