"""bfs.py 的单元测试"""

from puzzle_core.constants import GOAL, RIGHT
from puzzle_core.operators import get_neighbors
from puzzle_core.search.bfs import bfs
from puzzle_core.state import parse_state

# 距目标 10 步，最优解已用穷举 BFS 核对过
TEN_MOVES = (1, 6, 2, 5, 7, 3, 0, 4, 8)


def test_start_equals_goal():
    result = bfs(GOAL)
    assert result.algorithm == "bfs"
    assert result.found
    assert result.path == [GOAL]
    assert result.actions == []

def test_two_moves_away():
    start = parse_state("1 2 3 4 5 6 0 7 8")
    result = bfs(start)
    assert result.found
    assert result.actions == [RIGHT, RIGHT]
    assert result.path[0] == start
    assert result.path[-1] == GOAL

def test_ten_moves_away_is_optimal():
    result = bfs(TEN_MOVES)
    assert result.found
    assert len(result.actions) == 10
    assert result.path[0] == TEN_MOVES
    assert result.path[-1] == GOAL

def test_path_is_connected_by_legal_moves():
    result = bfs(TEN_MOVES)
    for before, after in zip(result.path, result.path[1:]):
        assert any(state == after for _, state in get_neighbors(before))

def test_counters_recorded():
    result = bfs(parse_state("1 2 3 4 5 6 0 7 8"))
    assert result.expanded >= 1
    assert result.generated >= 2
    assert result.peak_frontier >= 1
    assert result.elapsed_ms >= 0.0