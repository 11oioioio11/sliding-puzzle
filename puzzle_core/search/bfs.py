"""广度优先搜索 (BFS)。

警告：保证找到最短路径，但空间复杂度极高，大规模状态下极易导致 OOM。
"""

from collections import deque
from time import perf_counter

from ..constants import GOAL
from ..operators import get_neighbors
from ..state import State
from .base import Node, SearchResult, reconstruct_path

def bfs(start: State, goal: State = GOAL) -> SearchResult:
    """使用广度优先搜索 (BFS) 寻找最短路径

    Warning:
        空间复杂度为 O(b^d)，状态空间极大时极易触发 OOM（内存溢出）
    """
    started = perf_counter()

    def elapsed() -> float:
        return (perf_counter() - started) * 1000.0

    if start == goal:
        return SearchResult(
            algorithm="bfs", found=True, path=[start], elapsed_ms=elapsed()    
            )

    root = Node(state = start)
    frontier: deque[Node] = deque([root])
    # 入队时即标记已访问：BFS 中首次到达某状态就是最短，后到的可以安全丢弃
    explored: set[State] = {start}
    expanded = 0
    generated = 0
    peak_frontier = 1

    while frontier:
        node = frontier.popleft()
        expanded += 1

        for action, next_state in get_neighbors(node.state):
            generated += 1
            if next_state in explored:
                continue

            child = Node(
                state=next_state,
                parent=node,
                action=action,
                depth=node.depth + 1,
                g=node.g + 1,
                )

            if next_state == goal:
                states, actions = reconstruct_path(child)
                return SearchResult(
                    algorithm="bfs",
                    found=True,
                    path=states,
                    actions=actions,
                    expanded=expanded,
                    generated=generated,
                    peak_frontier=peak_frontier,
                    elapsed_ms=elapsed(),
                    )

            explored.add(next_state)
            frontier.append(child)
            peak_frontier = max(peak_frontier, len(frontier))

    return SearchResult(
        algorithm="bfs",
        found=False,
        expanded=expanded,
        generated=generated,
        peak_frontier=peak_frontier,
        elapsed_ms=elapsed(),
        )