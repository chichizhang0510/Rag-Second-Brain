"""Legacy shim: prefer ``python -m src.cli ask --question '...'`` from $REPO_ROOT."""

from __future__ import annotations

import sys

from src.cli.main import main

if __name__ == "__main__":
    raise SystemExit(main())
