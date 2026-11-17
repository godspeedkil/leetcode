import pytest

from lc import build_list, build_tree, list_values, tree_values


@pytest.mark.parametrize("values", [[], [1], [1, 2, 3]])
def test_linked_list_round_trip(values):
    assert list_values(build_list(values)) == values


@pytest.mark.parametrize(
    "values",
    [[], [1], [1, 2, 3], [1, None, 2, 3], [5, 4, 8, 11, None, 13, 4]],
)
def test_tree_round_trip(values):
    assert tree_values(build_tree(values)) == values
