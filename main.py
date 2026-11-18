#!/usr/bin/env python3
"""Entry program for news-image-20261118.

Copies the front page image (entry.png, shipped in this repository) into
the output directory the grader provides. The image is checked before it
is written: it must start with the PNG magic bytes and its SHA-256 must
match the digest recorded below, so a corrupted or swapped file fails
loudly instead of submitting silently. Standard library only, no network.
"""
import hashlib
import os
import sys
from pathlib import Path

EXPECTED_SHA256 = "8ac0b7c1aa943ceb9dc45138fb9aa26cdf84b1796cc6041e3bcfe30608edb269"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def run():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        return fail("entry.png is missing from the repository")

    blob = source.read_bytes()
    if blob[:8] != PNG_MAGIC:
        return fail("entry.png does not start with the PNG magic bytes")
    if len(blob) > 1048576:
        return fail(f"entry.png is {len(blob)} bytes, over the 1 MiB cap")

    digest = hashlib.sha256(blob).hexdigest()
    if digest != EXPECTED_SHA256:
        return fail(f"entry.png sha256 mismatch: got {digest}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")

    target = Path(out_dir) / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(blob)

    # read the written file back and confirm it is byte-identical
    written = target.read_bytes()
    if written != blob:
        return fail("written entry.png differs from the source bytes")
    print(f"wrote {target} ({len(blob)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(run())
