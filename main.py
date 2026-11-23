from puzzle_core.board_utils import print_state
from puzzle_core.constants import GOAL
from puzzle_core.state import is_solvable

INITIAL_STATE = (1, 2, 3, 4, 5, 6, 0, 7, 8)

def main() -> None:
    print("初始状态:")
    print_state(INITIAL_STATE)
    print("目标状态:")
    print_state(GOAL)
    print(f"可解：{is_solvable(INITIAL_STATE)}")

if __name__ == "__main__":
    main()