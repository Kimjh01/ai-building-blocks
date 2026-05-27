# 15-ai-evaluation

## 목적

AI 결과 품질을 비교하고 기록하기 위한 평가 모듈 시작점입니다.

## 주요 기능

- 예측값과 정답 데이터를 나중에 연결하기 쉬운 구조
- 평가지표 계산 로직을 붙이기 위한 엔트리포인트
- 평가 결과를 공통 딕셔너리로 반환

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

예측 결과, 정답 데이터, 평가 기준

## Output

점수, 지표 요약, 상태 정보

## Example Output

```python
{
  "module": "15-ai-evaluation",
  "package": "ai_evaluation",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 정량 평가 지표 계산 추가
- 리포트 저장 로직 연결
