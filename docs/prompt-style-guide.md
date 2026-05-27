# Prompt Style Guide

## 목적

프롬프트를 여러 모듈에서 재사용할 수 있도록 일관된 작성 규칙을 유지합니다.

## 권장 규칙

- 역할을 한 문장으로 명확히 정의합니다.
- 입력 형식과 출력 형식을 분리해서 적습니다.
- 제약 조건은 bullet list로 짧게 씁니다.
- JSON 출력이 필요하면 키 이름과 타입을 미리 고정합니다.
- 프롬프트 안에 민감한 키나 실제 비밀값을 넣지 않습니다.

## 예시 틀

```text
Role:
You are a helpful assistant for ...

Input:
- user_goal:
- context:

Constraints:
- Keep the answer concise.
- Return JSON only.

Output Schema:
{
  "summary": "string",
  "confidence": 0.0
}
```
