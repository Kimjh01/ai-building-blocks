# 16-3d-reconstruction-helper

## 목적

3D 재구성 실험을 보조하는 전처리와 파일 정리용 기본 구조입니다.

## 주요 기능

- 입력 프레임과 산출 경로를 분리한 구조
- 전처리 단계와 외부 툴 호출을 붙이기 쉬운 엔트리포인트
- 실험 상태를 요약하는 결과 객체 제공

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

이미지 시퀀스, 카메라 정보, 재구성 설정

## Output

전처리 상태, 산출 경로, 메타정보

## Example Output

```python
{
  "module": "16-3d-reconstruction-helper",
  "package": "three_d_reconstruction_helper",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 전처리 로직 추가
- 외부 재구성 툴 연동 코드 추가
