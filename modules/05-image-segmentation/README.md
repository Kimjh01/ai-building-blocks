# 05-image-segmentation

## 목적

이미지 분할 모델 실험과 결과 저장을 위한 기본 구조입니다.

## 주요 기능

- 입력 이미지와 분할 결과 저장 경로를 분리한 구조
- 후처리와 시각화 단계를 붙이기 쉬운 엔트리포인트
- 실험 결과를 딕셔너리로 반환하는 최소 예시

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

원본 이미지, 모델 설정, 후처리 옵션

## Output

마스크 경로, 클래스 정보, 실행 상태

## Example Output

```python
{
  "module": "05-image-segmentation",
  "package": "image_segmentation",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 세그멘테이션 모델 연결
- 마스크 시각화 및 저장 로직 추가
