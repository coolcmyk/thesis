#!/usr/bin/env python3
"""Expand a multi-file LaTeX thesis into one review-only source document."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


INPUT_RE = re.compile(r"^(?P<indent>\s*)\\input\{(?P<path>[^}]+)\}")


def resolve_input(raw_path: str, parent: Path, root: Path) -> Path | None:
    """Resolve an input target relative to its parent, confined to the repo."""
    candidate = Path(raw_path)
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    candidate = (parent / candidate).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as error:
        raise ValueError(f"refusing to read input outside the repository: {raw_path}") from error
    return candidate if candidate.is_file() else None


def flatten(path: Path, root: Path, stack: tuple[Path, ...] = ()) -> str:
    """Recursively inline line-start LaTeX input directives."""
    if path in stack:
        chain = " -> ".join(str(item.relative_to(root)) for item in (*stack, path))
        raise ValueError(f"cyclic LaTeX input detected: {chain}")

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"cannot decode {path.relative_to(root)} as UTF-8") from error

    output: list[str] = []
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("%"):
            output.append(line)
            continue
        match = INPUT_RE.match(line)
        if not match:
            output.append(line)
            continue

        target = resolve_input(match.group("path"), path.parent, root)
        if target is None:
            output.append(line)
            continue

        relative = target.relative_to(root)
        output.append(f"\n% --- BEGIN INLINED: {relative} ---\n")
        output.append(flatten(target, root, (*stack, path)))
        output.append(f"\n% --- END INLINED: {relative} ---\n")

    return "".join(output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="root LaTeX source file")
    parser.add_argument("output", type=Path, help="flattened review-only output file")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root used to confine recursive inputs (default: current directory)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    source = args.source.resolve()
    output = args.output.resolve()
    try:
        source.relative_to(root)
        output.relative_to(root)
    except ValueError:
        print("source and output must both be inside --root", file=sys.stderr)
        return 2

    try:
        result = flatten(source, root)
    except (OSError, ValueError) as error:
        print(f"flattening failed: {error}", file=sys.stderr)
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(result, encoding="utf-8")
    print(f"wrote {output.relative_to(root)} ({len(result):,} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
