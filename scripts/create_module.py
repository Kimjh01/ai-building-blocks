from __future__ import annotations

import re
import sys
from pathlib import Path
from textwrap import dedent


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = REPO_ROOT / "modules"

NUMBER_WORDS = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
}

MODULE_METADATA = {
    "llm-chat": {
        "purpose": "대화형 LLM 기능을 빠르게 붙일 수 있는 최소 실행 골격을 제공합니다.",
        "features": [
            "시스템 프롬프트와 사용자 입력 흐름 시작점",
            "모델 호출 로직을 붙이기 쉬운 `main()` 엔트리포인트",
            "향후 대화 이력 관리와 툴 호출을 확장하기 위한 기본 구조",
        ],
        "input": "사용자 질문 텍스트, 시스템 프롬프트, API 키 같은 환경변수 설정",
        "output": "모델 응답, 실행 상태, 메타데이터를 담는 결과 딕셔너리",
        "todo": [
            "실제 LLM API 호출 로직 추가",
            "대화 히스토리 저장 구조 추가",
        ],
        "recommended": ["openai", "litellm", "tiktoken"],
    },
    "rag-doc-search": {
        "purpose": "문서 기반 검색과 응답 생성을 연결하는 RAG 파이프라인 출발점을 제공합니다.",
        "features": [
            "문서 로딩과 청킹 위치를 분리하기 쉬운 구조",
            "임베딩 생성과 검색 단계를 추가할 수 있는 시작점",
            "검색 결과와 답변 생성을 하나의 결과 객체로 반환",
        ],
        "input": "PDF나 텍스트 문서, 질의 문장, 임베딩 및 검색 설정",
        "output": "검색된 문서 조각, 응답 초안, 실행 메타정보",
        "todo": [
            "문서 로더와 청킹 로직 추가",
            "벡터 DB 연결 및 검색 단계 구현",
        ],
        "recommended": ["pypdf", "chromadb", "sentence-transformers"],
    },
    "prompt-template-manager": {
        "purpose": "프롬프트 템플릿을 모아두고 버전 관리하기 위한 시작 구조입니다.",
        "features": [
            "프롬프트 템플릿 저장소로 확장하기 쉬운 패키지 구조",
            "입력 변수와 렌더링 규칙을 붙이기 쉬운 엔트리포인트",
            "향후 템플릿 테스트와 배포 규칙을 추가하기 좋은 기본 뼈대",
        ],
        "input": "템플릿 이름, 템플릿 변수, 렌더링 옵션",
        "output": "렌더링된 프롬프트 문자열과 실행 상태 정보",
        "todo": [
            "템플릿 파일 로더 추가",
            "변수 검증 및 버전 관리 규칙 추가",
        ],
        "recommended": ["jinja2", "pyyaml", "pydantic-settings"],
    },
    "ocr-document-parser": {
        "purpose": "문서 이미지나 스캔본에서 텍스트를 추출하고 구조화하는 시작점입니다.",
        "features": [
            "OCR 입력과 후처리 결과를 분리하는 기본 구조",
            "문서 유형별 파서 확장을 고려한 엔트리포인트",
            "추출 텍스트와 메타정보를 결과 딕셔너리로 반환",
        ],
        "input": "문서 이미지, PDF 변환 이미지, OCR 설정",
        "output": "추출 텍스트, 문단 구조, 파싱 상태 정보",
        "todo": [
            "OCR 엔진 연결",
            "문서 레이아웃 후처리 로직 추가",
        ],
        "recommended": ["paddleocr", "pytesseract", "pillow"],
    },
    "image-segmentation": {
        "purpose": "이미지 분할 모델 실험과 결과 저장을 위한 기본 구조입니다.",
        "features": [
            "입력 이미지와 분할 결과 저장 경로를 분리한 구조",
            "후처리와 시각화 단계를 붙이기 쉬운 엔트리포인트",
            "실험 결과를 딕셔너리로 반환하는 최소 예시",
        ],
        "input": "원본 이미지, 모델 설정, 후처리 옵션",
        "output": "마스크 경로, 클래스 정보, 실행 상태",
        "todo": [
            "실제 세그멘테이션 모델 연결",
            "마스크 시각화 및 저장 로직 추가",
        ],
        "recommended": ["opencv-python", "pillow", "numpy"],
    },
    "pose-estimation": {
        "purpose": "사람 자세 추정 기능을 실험할 수 있는 기본 모듈 골격입니다.",
        "features": [
            "프레임 입력과 포즈 결과 출력을 분리한 구조",
            "관절 좌표 후처리와 스코어 계산 확장 가능",
            "간단한 결과 객체를 통해 파이프라인 연결 가능",
        ],
        "input": "이미지 또는 비디오 프레임, 추론 설정",
        "output": "관절 좌표, 신뢰도, 상태 정보",
        "todo": [
            "실제 포즈 추정 엔진 연결",
            "관절 후처리 및 시각화 추가",
        ],
        "recommended": ["opencv-python", "mediapipe", "numpy"],
    },
    "video-frame-extractor": {
        "purpose": "비디오에서 프레임을 추출해 다른 AI 모듈에 연결하는 시작점입니다.",
        "features": [
            "입력 비디오와 출력 프레임 경로를 분리한 구조",
            "샘플링 간격과 저장 규칙을 붙이기 쉬운 엔트리포인트",
            "추출 결과를 요약 딕셔너리로 반환",
        ],
        "input": "비디오 파일, FPS 또는 간격 설정, 출력 경로",
        "output": "추출 프레임 수, 저장 위치, 상태 정보",
        "todo": [
            "실제 프레임 추출 로직 추가",
            "샘플링 전략과 파일명 규칙 추가",
        ],
        "recommended": ["opencv-python", "ffmpeg-python", "numpy"],
    },
    "speech-to-text": {
        "purpose": "오디오 파일에서 텍스트를 추출하는 STT 기능 시작점입니다.",
        "features": [
            "오디오 입력과 전사 결과 저장 구조 제공",
            "언어 설정과 후처리 로직을 붙이기 쉬운 엔트리포인트",
            "전사 결과를 공통 딕셔너리 형태로 반환",
        ],
        "input": "오디오 파일, 언어 설정, 전사 옵션",
        "output": "전사 텍스트, 세그먼트 정보, 상태 정보",
        "todo": [
            "실제 STT 엔진 연결",
            "세그먼트 후처리와 타임스탬프 정리 추가",
        ],
        "recommended": ["faster-whisper", "soundfile"],
    },
    "text-to-speech": {
        "purpose": "텍스트를 오디오로 변환하는 TTS 기능 시작 구조입니다.",
        "features": [
            "입력 텍스트와 출력 오디오 경로를 분리한 구조",
            "음성 옵션과 저장 규칙을 붙이기 쉬운 엔트리포인트",
            "합성 결과를 딕셔너리로 반환",
        ],
        "input": "입력 텍스트, 음성 스타일, 출력 파일 설정",
        "output": "생성 오디오 경로, 길이 정보, 상태 정보",
        "todo": [
            "실제 TTS 엔진 연결",
            "음성 옵션 프리셋 추가",
        ],
        "recommended": ["edge-tts", "gTTS"],
    },
    "recommendation-engine": {
        "purpose": "추천 모델 실험과 후보 점수 계산을 위한 기본 골격입니다.",
        "features": [
            "입력 사용자 정보와 추천 결과를 분리한 구조",
            "룰 기반과 모델 기반 로직을 나중에 교체하기 쉬움",
            "추천 후보와 점수를 예시 결과로 반환",
        ],
        "input": "사용자 프로필, 아이템 목록, 추천 조건",
        "output": "추천 아이템 목록, 점수, 상태 정보",
        "todo": [
            "피처 전처리와 점수 계산 로직 추가",
            "오프라인 평가 스크립트 연결",
        ],
        "recommended": ["pandas", "scikit-learn", "numpy"],
    },
    "agent-workflow": {
        "purpose": "여러 AI 기능을 에이전트 단위로 묶어 실행하는 시작점입니다.",
        "features": [
            "작업 단계와 도구 호출 흐름을 추가하기 쉬운 구조",
            "에이전트 상태와 결과를 공통 딕셔너리로 반환",
            "향후 멀티스텝 워크플로와 툴 실행 관리 확장 가능",
        ],
        "input": "사용자 목표, 도구 설정, 실행 단계 정보",
        "output": "에이전트 결과, 사용 단계, 상태 정보",
        "todo": [
            "실제 툴 실행 체인 추가",
            "상태 관리와 리트라이 정책 추가",
        ],
        "recommended": ["openai", "litellm", "networkx"],
    },
    "api-server-template": {
        "purpose": "Python API 서버를 빠르게 시작하기 위한 최소 템플릿입니다.",
        "features": [
            "엔드포인트 추가를 고려한 기본 패키지 구조",
            "추후 설정, 라우터, 미들웨어 분리를 쉽게 만드는 시작점",
            "간단한 실행 결과 딕셔너리 반환 예시",
        ],
        "input": "HTTP 요청, 환경변수 기반 설정, 서비스 옵션",
        "output": "응답 데이터, 상태 메시지, 서버 메타정보",
        "todo": [
            "실제 웹 프레임워크 연결",
            "헬스체크와 기본 라우터 추가",
        ],
        "recommended": ["fastapi", "uvicorn"],
    },
    "fastapi-ai-service": {
        "purpose": "FastAPI 기반 AI 서비스 실험을 위한 시작 구조입니다.",
        "features": [
            "AI 추론 로직과 API 계층을 분리하기 쉬운 구조",
            "입력 검증과 응답 모델 확장을 고려한 엔트리포인트",
            "서비스 결과를 공통 딕셔너리로 반환",
        ],
        "input": "API 요청 바디, 모델 설정, 서비스 환경변수",
        "output": "추론 결과, 응답 메타정보, 상태 정보",
        "todo": [
            "FastAPI 앱과 라우터 추가",
            "요청/응답 스키마 세분화",
        ],
        "recommended": ["fastapi", "uvicorn"],
    },
    "vector-db-template": {
        "purpose": "임베딩 저장과 검색용 벡터 DB 실험 골격입니다.",
        "features": [
            "문서 입력과 인덱스 출력을 분리한 구조",
            "벡터 저장소 연결과 검색 단계를 붙이기 쉬움",
            "색인 상태를 요약 결과로 반환",
        ],
        "input": "문서 조각, 임베딩 벡터, 컬렉션 설정",
        "output": "인덱스 상태, 저장 건수, 검색 준비 정보",
        "todo": [
            "실제 벡터 DB 클라이언트 연결",
            "검색 및 삭제 API 추가",
        ],
        "recommended": ["chromadb", "faiss-cpu", "numpy"],
    },
    "ai-evaluation": {
        "purpose": "AI 결과 품질을 비교하고 기록하기 위한 평가 모듈 시작점입니다.",
        "features": [
            "예측값과 정답 데이터를 나중에 연결하기 쉬운 구조",
            "평가지표 계산 로직을 붙이기 위한 엔트리포인트",
            "평가 결과를 공통 딕셔너리로 반환",
        ],
        "input": "예측 결과, 정답 데이터, 평가 기준",
        "output": "점수, 지표 요약, 상태 정보",
        "todo": [
            "정량 평가 지표 계산 추가",
            "리포트 저장 로직 연결",
        ],
        "recommended": ["pandas", "scikit-learn", "deepeval"],
    },
    "3d-reconstruction-helper": {
        "purpose": "3D 재구성 실험을 보조하는 전처리와 파일 정리용 기본 구조입니다.",
        "features": [
            "입력 프레임과 산출 경로를 분리한 구조",
            "전처리 단계와 외부 툴 호출을 붙이기 쉬운 엔트리포인트",
            "실험 상태를 요약하는 결과 객체 제공",
        ],
        "input": "이미지 시퀀스, 카메라 정보, 재구성 설정",
        "output": "전처리 상태, 산출 경로, 메타정보",
        "todo": [
            "실제 전처리 로직 추가",
            "외부 재구성 툴 연동 코드 추가",
        ],
        "recommended": ["opencv-python", "numpy"],
    },
    "report-generator": {
        "purpose": "AI 결과를 사람이 읽기 쉬운 보고서로 변환하는 시작 구조입니다.",
        "features": [
            "입력 데이터와 최종 문서 출력을 분리한 구조",
            "템플릿 렌더링과 포맷 변환을 붙이기 쉬운 엔트리포인트",
            "리포트 생성 상태를 결과 객체로 반환",
        ],
        "input": "요약할 데이터, 리포트 템플릿, 출력 형식 설정",
        "output": "리포트 문자열 또는 파일 경로, 상태 정보",
        "todo": [
            "리포트 템플릿 렌더링 추가",
            "Markdown/HTML/PDF 출력 단계 추가",
        ],
        "recommended": ["jinja2", "markdown", "pandas"],
    },
}


def usage() -> None:
    print("Usage: python scripts/create_module.py 18-new-ai-module")


def remove_index_prefix(module_name: str) -> str:
    return re.sub(r"^\d+-", "", module_name.strip().lower())


def digits_to_words(text: str) -> str:
    if text in NUMBER_WORDS:
        return NUMBER_WORDS[text]
    return "_".join(NUMBER_WORDS[digit] for digit in text if digit in NUMBER_WORDS)


def slug_to_package_name(slug: str) -> str:
    normalized = slug.lower().replace("-", "_")
    normalized = re.sub(r"(\d+)", lambda match: f"_{digits_to_words(match.group(1))}_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def slug_to_title(slug: str) -> str:
    parts = slug.split("-")
    return " ".join(part.upper() if len(part) <= 4 else part.title() for part in parts)


def get_metadata(slug: str) -> dict[str, object]:
    default = {
        "purpose": "새 AI 기능을 빠르게 실험하기 위한 기본 모듈 골격입니다.",
        "features": [
            "입력과 출력 디렉토리를 분리한 최소 구조",
            "확장 가능한 `main()` 엔트리포인트 제공",
            "테스트와 문서를 함께 시작할 수 있는 기본 스캐폴드",
        ],
        "input": "기능 구현에 필요한 입력 데이터와 환경변수",
        "output": "실행 결과를 담는 딕셔너리와 산출물 파일",
        "todo": [
            "실제 기능 로직 추가",
            "입출력 스키마와 테스트 확장",
        ],
        "recommended": ["requests", "numpy", "pandas"],
    }
    return MODULE_METADATA.get(slug, default)


def build_readme(module_name: str, package_name: str, metadata: dict[str, object]) -> str:
    features = "\n".join(f"- {item}" for item in metadata["features"])
    todos = "\n".join(f"- {item}" for item in metadata["todo"])
    example_output = dedent(
        f"""\
        {{
          "module": "{module_name}",
          "package": "{package_name}",
          "status": "ok",
          "message": "확장 가능한 기본 결과입니다."
        }}
        """
    ).strip()

    return "\n".join(
        [
            f"# {module_name}",
            "",
            "## 목적",
            "",
            str(metadata["purpose"]),
            "",
            "## 주요 기능",
            "",
            features,
            "",
            "## Setup",
            "",
            "```bash",
            "uv venv",
            "uv pip install -e ../../shared",
            "uv pip install -e .",
            "```",
            "",
            "## Run",
            "",
            "```bash",
            "python run.py",
            "```",
            "",
            "## Input",
            "",
            str(metadata["input"]),
            "",
            "## Output",
            "",
            str(metadata["output"]),
            "",
            "## Example Output",
            "",
            "```python",
            example_output,
            "```",
            "",
            "## TODO",
            "",
            todos,
        ]
    )


def build_pyproject(project_name: str, module_name: str, metadata: dict[str, object]) -> str:
    recommended = ", ".join(metadata["recommended"])
    return dedent(
        f"""\
        [build-system]
        requires = ["setuptools>=68"]
        build-backend = "setuptools.build_meta"

        [project]
        name = "{project_name}"
        version = "0.1.0"
        description = "Scaffold module for {module_name}"
        readme = "README.md"
        requires-python = ">=3.10"
        dependencies = [
            "pydantic",
            "python-dotenv",
        ]

        # 추천 의존성: {recommended}

        [tool.setuptools.packages.find]
        where = ["src"]
        """
    )


def build_env_example(module_name: str) -> str:
    return dedent(
        f"""\
        MODULE_NAME={module_name}
        LOG_LEVEL=INFO
        INPUT_DIR=./data/input
        OUTPUT_DIR=./data/output
        SERVICE_API_KEY=your_service_api_key
        """
    )


def build_run_py(package_name: str) -> str:
    return dedent(
        f"""\
        from __future__ import annotations

        import sys
        from pathlib import Path
        from pprint import pprint

        SRC_DIR = Path(__file__).resolve().parent / "src"
        if str(SRC_DIR) not in sys.path:
            sys.path.insert(0, str(SRC_DIR))

        from {package_name}.main import main


        if __name__ == "__main__":
            pprint(main())
        """
    )


def build_package_init(package_name: str) -> str:
    return dedent(
        f"""\
        from .main import MODULE_NAME, main

        __all__ = ["MODULE_NAME", "main"]
        """
    )


def build_main_py(module_name: str, package_name: str) -> str:
    return dedent(
        f"""\
        from __future__ import annotations

        from pprint import pprint

        MODULE_NAME = "{module_name}"
        PACKAGE_NAME = "{package_name}"


        def main() -> dict[str, str]:
            print(f"Running module: {{MODULE_NAME}}")
            return {{
                "module": MODULE_NAME,
                "package": PACKAGE_NAME,
                "status": "ok",
                "message": "확장 가능한 기본 결과입니다.",
            }}


        if __name__ == "__main__":
            pprint(main())
        """
    )


def build_test_py(package_name: str, module_name: str) -> str:
    return dedent(
        f"""\
        from __future__ import annotations

        import sys
        from pathlib import Path

        SRC_DIR = Path(__file__).resolve().parents[1] / "src"
        if str(SRC_DIR) not in sys.path:
            sys.path.insert(0, str(SRC_DIR))

        from {package_name}.main import main


        def test_basic() -> None:
            result = main()
            assert result["module"] == "{module_name}"
            assert result["package"] == "{package_name}"
            assert result["status"] == "ok"
        """
    )


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def touch_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8", newline="\n")


def create_module(module_name: str) -> Path:
    if not module_name or "/" in module_name or "\\" in module_name:
        raise ValueError("Module name must be a simple folder name such as 18-new-ai-module.")

    slug = remove_index_prefix(module_name)
    project_name = slug
    package_name = slug_to_package_name(slug)
    metadata = get_metadata(slug)

    module_dir = MODULES_DIR / module_name
    if module_dir.exists():
        raise FileExistsError(f"Module already exists: {module_dir}")

    (module_dir / "data" / "input").mkdir(parents=True, exist_ok=True)
    (module_dir / "data" / "output").mkdir(parents=True, exist_ok=True)
    (module_dir / "notebooks").mkdir(parents=True, exist_ok=True)
    (module_dir / "src" / package_name).mkdir(parents=True, exist_ok=True)
    (module_dir / "tests").mkdir(parents=True, exist_ok=True)

    touch_file(module_dir / "data" / "input" / ".gitkeep")
    touch_file(module_dir / "data" / "output" / ".gitkeep")
    touch_file(module_dir / "notebooks" / ".gitkeep")

    write_file(module_dir / "README.md", build_readme(module_name, package_name, metadata))
    write_file(module_dir / "pyproject.toml", build_pyproject(project_name, module_name, metadata))
    write_file(module_dir / ".env.example", build_env_example(module_name))
    write_file(module_dir / "run.py", build_run_py(package_name))
    write_file(module_dir / "src" / package_name / "__init__.py", build_package_init(package_name))
    write_file(module_dir / "src" / package_name / "main.py", build_main_py(module_name, package_name))
    write_file(module_dir / "tests" / "test_basic.py", build_test_py(package_name, module_name))

    return module_dir


def main() -> int:
    if len(sys.argv) != 2:
        usage()
        return 1

    module_name = sys.argv[1].strip()
    try:
        module_dir = create_module(module_name)
    except (ValueError, FileExistsError) as error:
        print(error)
        return 1

    title = slug_to_title(remove_index_prefix(module_name))
    print(f"Created module: {module_dir}")
    print(f"Package name: {slug_to_package_name(remove_index_prefix(module_name))}")
    print(f"Display title: {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
