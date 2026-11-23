from puzzle_core.board_utils import print_state

# 定义目标状态（0表示空格）
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# 定义初始状态
INITIAL_STATE = (1, 2, 3, 4, 5, 6, 0, 7, 8)

# 测试打印
print("初始状态:")
print_state(INITIAL_STATE)
print("目标状态:")
print_state(GOAL_STATE)