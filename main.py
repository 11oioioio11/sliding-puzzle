"""命令行入口：演示用 BFS 求解。"""

from puzzle_core.board_utils import print_result, print_state
from puzzle_core.search.bfs import bfs

INITIAL_STATE = (1, 6, 2, 5, 7, 3, 0, 4, 8)


def main() -> None:
    print("初始状态:")
    print_state(INITIAL_STATE)

    result = bfs(INITIAL_STATE)
    print_result(result, trace=True)


if __name__ == "__main__":
    main()