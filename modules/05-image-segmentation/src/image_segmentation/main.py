from __future__ import annotations

from pprint import pprint

MODULE_NAME = "05-image-segmentation"
PACKAGE_NAME = "image_segmentation"


def main() -> dict[str, str]:
    print(f"Running module: {MODULE_NAME}")
    return {
        "module": MODULE_NAME,
        "package": PACKAGE_NAME,
        "status": "ok",
        "message": "확장 가능한 기본 결과입니다.",
    }


if __name__ == "__main__":
    pprint(main())
