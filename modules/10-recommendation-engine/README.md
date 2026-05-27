# 10-recommendation-engine

## 목적

추천 모델 실험과 후보 점수 계산을 위한 기본 골격입니다.

## 주요 기능

- 입력 사용자 정보와 추천 결과를 분리한 구조
- 룰 기반과 모델 기반 로직을 나중에 교체하기 쉬움
- 추천 후보와 점수를 예시 결과로 반환

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

사용자 프로필, 아이템 목록, 추천 조건

## Output

추천 아이템 목록, 점수, 상태 정보

## Example Output

```python
{
  "module": "10-recommendation-engine",
  "package": "recommendation_engine",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 피처 전처리와 점수 계산 로직 추가
- 오프라인 평가 스크립트 연결
