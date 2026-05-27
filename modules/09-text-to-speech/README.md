# 09-text-to-speech

## 목적

텍스트를 오디오로 변환하는 TTS 기능 시작 구조입니다.

## 주요 기능

- 입력 텍스트와 출력 오디오 경로를 분리한 구조
- 음성 옵션과 저장 규칙을 붙이기 쉬운 엔트리포인트
- 합성 결과를 딕셔너리로 반환

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

입력 텍스트, 음성 스타일, 출력 파일 설정

## Output

생성 오디오 경로, 길이 정보, 상태 정보

## Example Output

```python
{
  "module": "09-text-to-speech",
  "package": "text_to_speech",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 TTS 엔진 연결
- 음성 옵션 프리셋 추가
