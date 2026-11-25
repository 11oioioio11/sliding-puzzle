"""
1. 棋盘显示工具：负责将一维状态数据可视化为终端文本
"""

from .search.base import SearchResult

from .constants import SIZE, CELLS, BLANK
from .state import State


def print_state(state: State) -> None:
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

def print_result(result: SearchResult, *, trace: bool = False) -> None:
    """打印搜索结果；trace 为真时逐步打印路径上的每个棋盘"""
    print("=" * 40)
    print(f"算法：{result.algorithm}")
    print(f"是否可解：{result.found}")
    if result.found:
        print(f"步数：{len(result.actions)}")
        print(f"动作：{' -> '.join(result.actions)}")
        if trace:
            for step, state in enumerate(result.path):
                print(f"第{step}步")
                print_state(state)
    print(
        f"实际搜索的Node数：{result.expanded}  生成的Node数：{result.generated}  "
        f"队列峰值：{result.peak_frontier}  耗时：{result.elapsed_ms:.2f} ms"
        )