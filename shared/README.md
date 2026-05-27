# shared

`shared/`는 여러 AI 모듈에서 공통으로 재사용할 유틸리티 패키지입니다. 환경변수 로드, 로깅, 파일 처리, JSON 처리, API 클라이언트 뼈대 같은 최소 기능을 포함합니다.

## 포함 항목

- `config.py`: `.env` 로드와 환경변수 조회
- `logger.py`: 공통 로거 생성
- `file_utils.py`: 텍스트 파일과 디렉토리 유틸
- `json_utils.py`: JSON 읽기/쓰기
- `image_utils.py`: 이미지 처리용 플레이스홀더
- `video_utils.py`: 비디오 처리용 플레이스홀더
- `api_client.py`: 확장 가능한 기본 API 클라이언트
- `types.py`: 공통 응답 모델 예시

## 설치

```bash
uv pip install -e ./shared
```

모듈 안에서는 아래처럼 설치합니다.

```bash
uv pip install -e ../../shared
```
