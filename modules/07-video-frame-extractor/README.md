# 07-video-frame-extractor

## 목적

비디오에서 프레임을 추출해 다른 AI 모듈에 연결하는 시작점입니다.

## 주요 기능

- 입력 비디오와 출력 프레임 경로를 분리한 구조
- 샘플링 간격과 저장 규칙을 붙이기 쉬운 엔트리포인트
- 추출 결과를 요약 딕셔너리로 반환

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

비디오 파일, FPS 또는 간격 설정, 출력 경로

## Output

추출 프레임 수, 저장 위치, 상태 정보

## Example Output

```python
{
  "module": "07-video-frame-extractor",
  "package": "video_frame_extractor",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 프레임 추출 로직 추가
- 샘플링 전략과 파일명 규칙 추가
