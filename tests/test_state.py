"""state.py 的单元测试。"""

import pytest

from puzzle_core.constants import GOAL
from puzzle_core.state import (
    blank_index,
    inversions,
    is_goal,
    is_solvable,
    parse_state,
    row_col,
)

# TODO：2026-11-23 完成测试代码，通过后提交上传

@pytest.mark.parametrize("raw_text", [
    "1 2 3 | 4 5 6 | 7 8 0",
    "1,2,3\n4,5,6\n7,8,0",
])
def test_parse_state_flexible_input(raw_text):
    assert parse_state(raw_text) == GOAL

@pytest.mark.parametrize("text",["1 2 3", "1 2 3 4 5 6 7 8 8", "1 2 3 4 5 6 7 8 9", "-1 2 3 4 5 6 7 8 0"], )
def test_parse_state_rejects_invalid(text):
    with pytest.raises(ValueError):
        parse_state(text)

def test_is_goal():
    assert is_goal(GOAL)
    assert not is_goal((1, 2, 3, 4, 5, 6, 7, 0, 8))

def test_inversions_ignores_blank():
    assert inversions((2, 1, 3, 4, 5, 6, 7, 8, 0)) == 1
    assert inversions((GOAL)) == 0

def test_is_solvable():
    assert is_solvable((1, 2, 3, 4, 5, 6, 7, 8, 0))
    assert is_solvable((3, 1, 2, 4, 5, 6, 7, 8, 0))
    assert not is_solvable((2, 1, 3, 4, 5, 6, 7, 8, 0))

def test_blank_index_and_row_col():
    state = parse_state("1 2 3 4 5 6 0 7 8")
    assert blank_index(state) == 6
    assert row_col(6) == (2, 0)
    assert row_col(4) == (1, 1)