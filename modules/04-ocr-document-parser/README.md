# 04-ocr-document-parser

## 목적

문서 이미지나 스캔본에서 텍스트를 추출하고 구조화하는 시작점입니다.

## 주요 기능

- OCR 입력과 후처리 결과를 분리하는 기본 구조
- 문서 유형별 파서 확장을 고려한 엔트리포인트
- 추출 텍스트와 메타정보를 결과 딕셔너리로 반환

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

문서 이미지, PDF 변환 이미지, OCR 설정

## Output

추출 텍스트, 문단 구조, 파싱 상태 정보

## Example Output

```python
{
  "module": "04-ocr-document-parser",
  "package": "ocr_document_parser",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- OCR 엔진 연결
- 문서 레이아웃 후처리 로직 추가
