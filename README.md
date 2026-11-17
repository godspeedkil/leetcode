# LeetCode

My LeetCode solutions. Each problem is one file in `problems/` with its
solution and test cases together.

## Setup

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
uv sync                        # creates .venv, installs Python 3.13 if needed
uv run pre-commit install      # run ruff on every commit
```

## Workflow

```sh
# 1. Scaffold a problem (slug is the part of the URL after /problems/)
uv run new 1 two-sum -d easy -t array hash-table

# 2. Paste LeetCode's method into Solution, add cases to the parametrize list

# 3. Test it
uv run pytest problems/0001_two_sum.py

# Everything
uv run pytest
uv run ruff check --fix . && uv run ruff format .
```

Useful pytest filters:

```sh
uv run pytest -k two_sum       # by name
uv run pytest -x               # stop at first failure
```

## Linked lists and trees

`lc` provides LeetCode's `ListNode` and `TreeNode`, plus converters so test
cases can use the same list notation as the problem page:

```python
from lc import ListNode, TreeNode, build_list, list_values, build_tree, tree_values

build_tree([1, None, 2, 3])  # level order, None for gaps
list_values(build_list([1, 2, 3]))  # [1, 2, 3]
```

## Finding problems

Each file's docstring has the difficulty and tags, so grep works:

```sh
grep -l "Difficulty: Hard" problems/*.py
grep -l "Tags:.*dp" problems/*.py
```

Problem statements aren't copied here, only a link to each one on leetcode.com.
