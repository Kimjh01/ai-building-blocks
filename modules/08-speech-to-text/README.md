# 08-speech-to-text

## 목적

오디오 파일에서 텍스트를 추출하는 STT 기능 시작점입니다.

## 주요 기능

- 오디오 입력과 전사 결과 저장 구조 제공
- 언어 설정과 후처리 로직을 붙이기 쉬운 엔트리포인트
- 전사 결과를 공통 딕셔너리 형태로 반환

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

오디오 파일, 언어 설정, 전사 옵션

## Output

전사 텍스트, 세그먼트 정보, 상태 정보

## Example Output

```python
{
  "module": "08-speech-to-text",
  "package": "speech_to_text",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 STT 엔진 연결
- 세그먼트 후처리와 타임스탬프 정리 추가
