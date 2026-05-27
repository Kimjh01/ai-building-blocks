# 11-agent-workflow

## 목적

여러 AI 기능을 에이전트 단위로 묶어 실행하는 시작점입니다.

## 주요 기능

- 작업 단계와 도구 호출 흐름을 추가하기 쉬운 구조
- 에이전트 상태와 결과를 공통 딕셔너리로 반환
- 향후 멀티스텝 워크플로와 툴 실행 관리 확장 가능

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

사용자 목표, 도구 설정, 실행 단계 정보

## Output

에이전트 결과, 사용 단계, 상태 정보

## Example Output

```python
{
  "module": "11-agent-workflow",
  "package": "agent_workflow",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 툴 실행 체인 추가
- 상태 관리와 리트라이 정책 추가
