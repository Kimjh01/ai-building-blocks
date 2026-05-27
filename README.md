# ai-building-blocks

프로젝트마다 반복해서 쓰게 되는 AI 기능을 재사용 가능한 모듈 단위로 정리하는 개인용 Python AI 모노레포입니다. 각 기능은 `modules/` 아래에서 독립적으로 관리하고, 공통 코드는 `shared/` 패키지로 분리해 확장하기 쉬운 구조를 목표로 합니다.

## GitHub Description

`A personal AI monorepo for reusable LLM, RAG, OCR, pose estimation, recommendation, and API service modules.`

## 목표

- 기능별 AI 모듈을 한 저장소에서 일관된 규칙으로 관리합니다.
- 각 모듈은 독립 가상환경에서 실행 가능하도록 유지합니다.
- 공통 유틸리티는 `shared/`에 모아 중복 구현을 줄입니다.
- 실제 데이터, 모델 파일, 로그, 환경변수 파일은 Git에서 제외합니다.
- 지금 당장 실행 가능한 최소 골격을 만들고, 이후 실제 기능을 붙이기 쉽게 설계합니다.

## 전체 폴더 구조

```text
ai-building-blocks/
├─ shared/
│  ├─ README.md
│  ├─ pyproject.toml
│  └─ src/
│     └─ ai_shared/
├─ modules/
│  ├─ 01-llm-chat/
│  ├─ 02-rag-doc-search/
│  ├─ 03-prompt-template-manager/
│  ├─ 04-ocr-document-parser/
│  ├─ 05-image-segmentation/
│  ├─ 06-pose-estimation/
│  ├─ 07-video-frame-extractor/
│  ├─ 08-speech-to-text/
│  ├─ 09-text-to-speech/
│  ├─ 10-recommendation-engine/
│  ├─ 11-agent-workflow/
│  ├─ 12-api-server-template/
│  ├─ 13-fastapi-ai-service/
│  ├─ 14-vector-db-template/
│  ├─ 15-ai-evaluation/
│  ├─ 16-3d-reconstruction-helper/
│  └─ 17-report-generator/
├─ examples/
│  ├─ fitness-posture-ai/
│  ├─ ai-date-course-recommender/
│  ├─ document-summary-service/
│  └─ obsidian-ai-automation/
├─ docs/
└─ scripts/
```

각 모듈은 아래 공통 구조를 따릅니다.

```text
모듈 폴더/
├─ README.md
├─ pyproject.toml
├─ .env.example
├─ run.py
├─ data/
│  ├─ input/
│  └─ output/
├─ notebooks/
├─ src/
│  └─ package_name/
└─ tests/
```

## 모듈 목록

| 번호 | 모듈 | 패키지 | 용도 |
| --- | --- | --- | --- |
| 01 | `01-llm-chat` | `llm_chat` | 기본 LLM 대화 흐름 시작점 |
| 02 | `02-rag-doc-search` | `rag_doc_search` | 문서 검색형 RAG 파이프라인 골격 |
| 03 | `03-prompt-template-manager` | `prompt_template_manager` | 프롬프트 템플릿 관리 |
| 04 | `04-ocr-document-parser` | `ocr_document_parser` | 문서 OCR 및 파싱 |
| 05 | `05-image-segmentation` | `image_segmentation` | 이미지 분할 실험 |
| 06 | `06-pose-estimation` | `pose_estimation` | 자세 추정 파이프라인 |
| 07 | `07-video-frame-extractor` | `video_frame_extractor` | 비디오 프레임 추출 |
| 08 | `08-speech-to-text` | `speech_to_text` | 음성 인식 |
| 09 | `09-text-to-speech` | `text_to_speech` | 음성 합성 |
| 10 | `10-recommendation-engine` | `recommendation_engine` | 추천 엔진 프로토타입 |
| 11 | `11-agent-workflow` | `agent_workflow` | 에이전트 기반 워크플로 |
| 12 | `12-api-server-template` | `api_server_template` | API 서버 시작 템플릿 |
| 13 | `13-fastapi-ai-service` | `fastapi_ai_service` | FastAPI 기반 AI 서비스 |
| 14 | `14-vector-db-template` | `vector_db_template` | 벡터 DB 연동 템플릿 |
| 15 | `15-ai-evaluation` | `ai_evaluation` | AI 결과 평가 |
| 16 | `16-3d-reconstruction-helper` | `three_d_reconstruction_helper` | 3D 재구성 보조 유틸 |
| 17 | `17-report-generator` | `report_generator` | 보고서 생성 자동화 |

## uv 기반 설치 방법

1. `uv`가 없다면 먼저 설치합니다.
2. 공통 패키지는 루트에서 아래처럼 설치합니다.

```bash
uv venv
uv pip install -e ./shared
```

3. 특정 모듈을 작업할 때는 해당 모듈 폴더로 이동해서 독립 환경을 만듭니다.

```bash
cd modules/01-llm-chat
uv venv
uv pip install -e ../../shared
uv pip install -e .
```

## 각 모듈 실행 방법

모든 모듈은 동일한 패턴으로 실행합니다.

```bash
cd modules/01-llm-chat
python run.py
```

또는 `uv`를 쓰는 경우:

```bash
cd modules/01-llm-chat
uv run python run.py
```

## shared 패키지 사용 방법

`shared/`는 여러 모듈에서 공통으로 쓰는 설정, 로거, 파일 처리 유틸을 담습니다.

```python
from ai_shared.config import get_env
from ai_shared.logger import get_logger

logger = get_logger("example")
api_key = get_env("OPENAI_API_KEY", default="")
```

모듈 환경에서 한 번만 아래처럼 설치하면 됩니다.

```bash
uv pip install -e ../../shared
```

## 새 모듈 추가 규칙

- 폴더명은 `번호-기능명` 형식을 따릅니다. 예: `18-new-ai-module`
- 패키지명은 숫자와 하이픈을 제거하고 `snake_case`로 만듭니다.
- 모든 모듈은 `README.md`, `pyproject.toml`, `run.py`, `src/`, `tests/`, `data/`, `notebooks/`를 포함합니다.
- 공통 로직은 가능하면 모듈 내부에 복붙하지 말고 `shared/`로 올립니다.
- 새 모듈은 아래 명령으로 생성합니다.

```bash
python scripts/create_module.py 18-new-ai-module
```

## Git에 올리면 안 되는 파일

다음 항목은 `.gitignore`로 제외합니다.

- `.env`, 모듈별 `.env`, 가상환경 폴더
- 입력/출력 데이터, 생성 산출물, 실험 로그
- 모델 파일(`.pt`, `.onnx`, `.ckpt`, `.bin`, `.safetensors`)
- 벡터 DB 인덱스(`chroma_db/`, `faiss_index/`)
- 캐시 디렉토리와 Jupyter 체크포인트

실제 API 키, 실제 학습 데이터, 대용량 모델 파일은 절대 커밋하지 않는 것을 전제로 합니다.
