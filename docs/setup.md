# Setup

## 1. uv 준비

```bash
uv --version
```

설치되어 있지 않다면 공식 가이드를 따라 `uv`를 먼저 설치합니다.

## 2. shared 설치

```bash
uv venv
uv pip install -e ./shared
```

## 3. 개별 모듈 설치

```bash
cd modules/01-llm-chat
uv venv
uv pip install -e ../../shared
uv pip install -e .
```

## 4. 테스트

```bash
python scripts/run_all_tests.py
```

## 5. 캐시 정리

```bash
python scripts/clean_cache.py
```
