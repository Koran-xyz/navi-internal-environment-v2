#!/usr/bin/env python3
"""NAVI WORK BOARD gateway.

Small runtime used by Goten/Admin to READ, APPEND and VERIFY the shared board.
The board backend is intentionally replaceable so the Navi system is not tied to
Notion, Google Drive, GitHub, or any specific AI platform.

Supported backends:
- file: a path in the External Free Region mounted on the machine
- http: a small board service exposing GET for read and POST for append

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import request, error


@dataclass
class Config:
    backend: str
    locator: str | None = None
    read_url: str | None = None
    append_url: str | None = None
    token_env: str | None = None

    @classmethod
    def load(cls, path: str) -> "Config":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(
            backend=raw["backend"],
            locator=raw.get("locator"),
            read_url=raw.get("read_url"),
            append_url=raw.get("append_url"),
            token_env=raw.get("token_env"),
        )


def _headers(cfg: Config) -> dict[str, str]:
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if cfg.token_env:
        token = os.environ.get(cfg.token_env)
        if token:
            headers["Authorization"] = f"Bearer {token}"
    return headers


def read_board(cfg: Config) -> str:
    if cfg.backend == "file":
        if not cfg.locator:
            raise RuntimeError("file backend requires locator")
        return Path(cfg.locator).read_text(encoding="utf-8")

    if cfg.backend == "http":
        if not cfg.read_url:
            raise RuntimeError("http backend requires read_url")
        req = request.Request(cfg.read_url, headers=_headers(cfg), method="GET")
        try:
            with request.urlopen(req, timeout=20) as res:
                body = res.read().decode("utf-8")
        except error.URLError as exc:
            raise RuntimeError(f"board read failed: {exc}") from exc
        try:
            parsed = json.loads(body)
            if isinstance(parsed, dict) and isinstance(parsed.get("content"), str):
                return parsed["content"]
        except json.JSONDecodeError:
            pass
        return body

    raise RuntimeError(f"unsupported backend: {cfg.backend}")


def append_board(cfg: Config, text: str) -> None:
    if cfg.backend == "file":
        if not cfg.locator:
            raise RuntimeError("file backend requires locator")
        board = Path(cfg.locator)
        board.parent.mkdir(parents=True, exist_ok=True)
        with board.open("a", encoding="utf-8", newline="\n") as f:
            if board.exists() and board.stat().st_size > 0:
                f.write("\n\n")
            f.write(text.rstrip() + "\n")
        return

    if cfg.backend == "http":
        if not cfg.append_url:
            raise RuntimeError("http backend requires append_url")
        payload = json.dumps({"operation": "append", "content": text}, ensure_ascii=False).encode("utf-8")
        req = request.Request(cfg.append_url, data=payload, headers=_headers(cfg), method="POST")
        try:
            with request.urlopen(req, timeout=20) as res:
                if not 200 <= res.status < 300:
                    raise RuntimeError(f"board append failed: HTTP {res.status}")
        except error.URLError as exc:
            raise RuntimeError(f"board append failed: {exc}") from exc
        return

    raise RuntimeError(f"unsupported backend: {cfg.backend}")


def build_entry(actor: str, status: str, done: str, current: str, next_action: str) -> str:
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    return (
        f"【{actor} 作業記録】\n\n"
        f"■ 状態（ステータス）\n・【{status}】\n\n"
        f"■ 今回やったこと\n・{done}\n\n"
        f"■ 現在地\n{current}\n\n"
        f"■ 次の作業\n・{next_action}\n\n"
        f"■ 更新日時\n{now}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="NAVI WORK BOARD gateway")
    parser.add_argument("--config", default="runtime/board_locator.json")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("read")

    append = sub.add_parser("append")
    append.add_argument("--actor", required=True)
    append.add_argument("--status", required=True)
    append.add_argument("--done", required=True)
    append.add_argument("--current", required=True)
    append.add_argument("--next", dest="next_action", required=True)

    verify = sub.add_parser("verify")
    verify.add_argument("--contains", required=True)

    args = parser.parse_args()
    cfg = Config.load(args.config)

    if args.command == "read":
        print(read_board(cfg))
        return 0

    if args.command == "append":
        entry = build_entry(args.actor, args.status, args.done, args.current, args.next_action)
        append_board(cfg, entry)
        print("APPEND_OK")
        return 0

    if args.command == "verify":
        board = read_board(cfg)
        if args.contains in board:
            print("VERIFY_OK")
            return 0
        print("VERIFY_NOT_FOUND")
        return 2

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
