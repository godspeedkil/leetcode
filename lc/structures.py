"""LeetCode's ListNode / TreeNode, plus converters to and from plain lists.

LeetCode writes linked lists as [1, 2, 3] and trees in level order with
None for gaps, e.g. [1, None, 2, 3]. These helpers let tests use the same
notation as the problem page.
"""

from __future__ import annotations

from collections import deque


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({list_values(self)})"


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({tree_values(self)})"


def build_list(values: list[int]) -> ListNode | None:
    """[1, 2, 3] -> 1 -> 2 -> 3"""
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def list_values(head: ListNode | None) -> list[int]:
    """1 -> 2 -> 3 -> [1, 2, 3]"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Level-order list (LeetCode format) -> tree."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_values(root: TreeNode | None) -> list[int | None]:
    """Tree -> level-order list (LeetCode format, trailing Nones removed)."""
    out: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out
