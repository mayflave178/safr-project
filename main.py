"""SAFR — точка входа приложения."""
from __future__ import annotations

import argparse
import sys


def _headless() -> int:
    from safr.infrastructure.logger import setup_logger
    from safr.infrastructure.paths import ensure_runtime_dirs
    from safr.infrastructure.config import CONFIG
    from safr.core.registry import create_default_registry

    ensure_runtime_dirs()
    log = setup_logger()
    log.info("%s v%s starting (headless self-check).",
             CONFIG.app_name, CONFIG.version)
    reg = create_default_registry()
    log.info("Registry ready: %s", reg)
    for kind, names in (("signals", reg.list_signals()),
                        ("noises", reg.list_noises()),
                        ("filters", reg.list_filters())):
        log.info("  %s: %s", kind, ", ".join(names))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SAFR launcher")
    parser.add_argument("--headless", action="store_true",
                        help="проверка ядра без запуска GUI")
    args = parser.parse_args()

    if args.headless:
        return _headless()

    from safr.app import run_gui
    return run_gui()


if __name__ == "__main__":
    sys.exit(main())