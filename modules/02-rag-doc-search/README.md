# 02-rag-doc-search

## 목적

문서 기반 검색과 응답 생성을 연결하는 RAG 파이프라인 출발점을 제공합니다.

## 주요 기능

- 문서 로딩과 청킹 위치를 분리하기 쉬운 구조
- 임베딩 생성과 검색 단계를 추가할 수 있는 시작점
- 검색 결과와 답변 생성을 하나의 결과 객체로 반환

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

PDF나 텍스트 문서, 질의 문장, 임베딩 및 검색 설정

## Output

검색된 문서 조각, 응답 초안, 실행 메타정보

## Example Output

```python
{
  "module": "02-rag-doc-search",
  "package": "rag_doc_search",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 문서 로더와 청킹 로직 추가
- 벡터 DB 연결 및 검색 단계 구현
