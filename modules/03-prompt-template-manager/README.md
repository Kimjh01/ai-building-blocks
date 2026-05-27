# 03-prompt-template-manager

## 목적

프롬프트 템플릿을 모아두고 버전 관리하기 위한 시작 구조입니다.

## 주요 기능

- 프롬프트 템플릿 저장소로 확장하기 쉬운 패키지 구조
- 입력 변수와 렌더링 규칙을 붙이기 쉬운 엔트리포인트
- 향후 템플릿 테스트와 배포 규칙을 추가하기 좋은 기본 뼈대

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

템플릿 이름, 템플릿 변수, 렌더링 옵션

## Output

렌더링된 프롬프트 문자열과 실행 상태 정보

## Example Output

```python
{
  "module": "03-prompt-template-manager",
  "package": "prompt_template_manager",
  "status": "ok",
  "message": "확장 가능한 기본 결과입니다."
}
```

## TODO

- 템플릿 파일 로더 추가
- 변수 검증 및 버전 관리 규칙 추가
