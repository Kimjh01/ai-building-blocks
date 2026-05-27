from __future__ import annotations

import runpy
import sys
import traceback
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = REPO_ROOT / "modules"


def list_modules() -> list[Path]:
    return sorted(path for path in MODULES_DIR.iterdir() if path.is_dir())


def list_test_files(module_dir: Path) -> list[Path]:
    tests_dir = module_dir / "tests"
    return sorted(tests_dir.glob("test_*.py")) if tests_dir.exists() else []


def run_test_file(test_file: Path) -> int:
    namespace = runpy.run_path(str(test_file))
    failures = 0
    for name, value in namespace.items():
        if not name.startswith("test_") or not callable(value):
            continue
        try:
            value()
            print(f"  [PASS] {test_file.name}::{name}")
        except Exception:
            failures += 1
            print(f"  [FAIL] {test_file.name}::{name}")
            traceback.print_exc()
    return failures


def run_module_tests(module_dir: Path) -> int:
    print(f"[TEST] {module_dir.name}")
    failures = 0
    test_files = list_test_files(module_dir)
    if not test_files:
        print("  [SKIP] No test files found.")
        return failures

    for test_file in test_files:
        failures += run_test_file(test_file)
    return failures


def main() -> int:
    failed_modules: list[str] = []
    for module_dir in list_modules():
        if run_module_tests(module_dir) > 0:
            failed_modules.append(module_dir.name)

    if failed_modules:
        print("Failed modules:")
        for name in failed_modules:
            print(f"- {name}")
        return 1

    print("All module tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
