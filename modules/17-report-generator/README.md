# 17-report-generator

## 목적

AI 결과를 사람이 읽기 쉬운 보고서로 변환하는 시작 구조입니다.

## 주요 기능

- 입력 데이터와 최종 문서 출력을 분리한 구조
- 템플릿 렌더링과 포맷 변환을 붙이기 쉬운 엔트리포인트
- 리포트 생성 상태를 결과 객체로 반환

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

요약할 데이터, 리포트 템플릿, 출력 형식 설정

## Output

리포트 문자열 또는 파일 경로, 상태 정보

## Example Output

```python
{
  "module": "17-report-generator",
  "package": "report_generator",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 리포트 템플릿 렌더링 추가
- Markdown/HTML/PDF 출력 단계 추가
