"""Scaffold a new problem file.

    uv run new 1 two-sum --difficulty easy --tags array hash-table

creates problems/0001_two_sum.py with a link, difficulty, tags,
a Solution stub and an empty parametrized test.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"

TEMPLATE = '''\
"""
{number}. {title}
https://leetcode.com/problems/{slug}/

Difficulty: {difficulty}
Tags: {tags}
"""

import pytest


class Solution:
    """
    Approach:

    Time:
    Space:
    """
    def solve(self):
        pass


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        # ((arg1, arg2), expected),
    ],
)
def test_solution(args, expected):
    assert Solution().solve(*args) == expected
'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a new LeetCode problem file.")
    parser.add_argument("number", type=int, help="problem number, e.g. 1")
    parser.add_argument("slug", help="URL slug from leetcode.com, e.g. two-sum")
    parser.add_argument(
        "-d",
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default="medium",
    )
    parser.add_argument("-t", "--tags", nargs="*", default=[], help="e.g. array dp")
    args = parser.parse_args(argv)

    slug = args.slug.strip().strip("/").split("/")[-1].lower()
    path = PROBLEMS_DIR / f"{args.number:04d}_{slug.replace('-', '_')}.py"
    if path.exists():
        print(f"Already exists: {path.relative_to(PROBLEMS_DIR.parent)}")
        return 1

    PROBLEMS_DIR.mkdir(exist_ok=True)
    path.write_text(
        TEMPLATE.format(
            number=args.number,
            title=slug.replace("-", " ").title(),
            slug=slug,
            difficulty=args.difficulty.title(),
            tags=", ".join(args.tags) or "-",
        )
    )
    print(f"Created {path.relative_to(PROBLEMS_DIR.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
