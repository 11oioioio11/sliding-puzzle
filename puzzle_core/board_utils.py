"""
1. 棋盘显示工具：负责将一维状态数据可视化为终端文本
"""

from .constants import SIZE, CELLS, BLANK, GOAL
from .state import State

def print_state(state):
    """
    辅助函数，将一维元组打印成二维的矩阵
    """

    # 用一个“假”的行来算出真实的字符串长度
    # 假设每个格子占 2 个字符宽，中间用 " | " 连接，两边有 "| " 和 " |"
    sample_row = "| " + " | ".join("  " for _ in range(SIZE)) + " |"
    divider = "-" * len(sample_row)  # 量出长度，动态生成横线

    print(divider)

    for i in range(0, CELLS, SIZE):
        row = state[i : i + SIZE]
        # 把 0 替换成空白字符，方便查看
        row_str = [f"{x:2}" if x != BLANK else "  " for x in row]
        # 动态拼接当前行：用 " | " 把列表里的元素连接起来
        row_text = " | ".join(row_str)
        # 打印整行
        print(f"| {row_text} |")

    print(divider + "\n")

if __name__ == "__main__":
    test_state = GOAL
    print_state(test_state)