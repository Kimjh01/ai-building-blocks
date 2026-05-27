# 06-pose-estimation

## 목적

사람 자세 추정 기능을 실험할 수 있는 기본 모듈 골격입니다.

## 주요 기능

- 프레임 입력과 포즈 결과 출력을 분리한 구조
- 관절 좌표 후처리와 스코어 계산 확장 가능
- 간단한 결과 객체를 통해 파이프라인 연결 가능

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

이미지 또는 비디오 프레임, 추론 설정

## Output

관절 좌표, 신뢰도, 상태 정보

## Example Output

```python
{
  "module": "06-pose-estimation",
  "package": "pose_estimation",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 포즈 추정 엔진 연결
- 관절 후처리 및 시각화 추가
