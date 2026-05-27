# 14-vector-db-template

## 목적

임베딩 저장과 검색용 벡터 DB 실험 골격입니다.

## 주요 기능

- 문서 입력과 인덱스 출력을 분리한 구조
- 벡터 저장소 연결과 검색 단계를 붙이기 쉬움
- 색인 상태를 요약 결과로 반환

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

문서 조각, 임베딩 벡터, 컬렉션 설정

## Output

인덱스 상태, 저장 건수, 검색 준비 정보

## Example Output

```python
{
  "module": "14-vector-db-template",
  "package": "vector_db_template",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 실제 벡터 DB 클라이언트 연결
- 검색 및 삭제 API 추가
