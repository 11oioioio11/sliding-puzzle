"""
1. 状态层：拼图核心状态的表示与基础操作。

2. 本模块负责状态（一维元组）的定义、解析、合法性校验、
以及影响搜索算法的数学属性（如逆序数、可解性判断）。

3. 架构依赖：
    1. 仅依赖 constants 模块，绝对不导入 search 等其他模块，防范循环引用。
    2. 供搜索算法（search）与展示工具（board_utils）调用。
"""

import re
from .constants import BLANK, CELLS, GOAL, SIZE

type State = tuple[int, ...]

def parse_state(text: str) -> State:
    """
    把 "1 2 3 | 4 5 6 | 7 8 0" 解析成状态元组。

    Raises:
        ValueError: 数字个数不是 CELLS，或 0..CELLS-1 没有各出现一次。
    
    """
    numbers = [int(token) for token in re.findall(r"-?\d+", text)]
    if len(numbers) != CELLS or sorted(numbers) != list(range(CELLS)):
        raise ValueError(
            f"需要 0..{CELLS - 1} 各一次，共 {CELLS} 个数，收到: {numbers}"
        )
    return tuple(numbers)

def is_goal(state: State, goal: State = GOAL) -> bool:
    """判断状态是否为目标状态。"""
    return state == goal

def inversions(state: State) -> int:
    """
    忽略空格，计算状态的逆序数。
    逆序数是指在状态中，前面的数字大于后面的数字的对数。
    """
    tiles = [tile for tile in state if tile != BLANK]
    count = 0
    for i in range(len(tiles)):
        for j in range(i + 1,len(tiles)):
            if tiles[i] > tiles[j]:
                count += 1
    return count

def is_solvable(state: State,goal: State = GOAL) -> bool:
    """
    判断状态是否可解。
    对于奇数阶的问题，将空格拿掉后，如果初始状态和目标状态的逆序数的奇偶性相同，则可解。
    TODO: 目前只支持奇数阶的八数码问题，偶数阶的情况需要考虑空格所在行数。
    """
    return (inversions(state) % 2) == (inversions(goal) % 2)

def blank_index(state: State) -> int:
    """空格（0）所在的下标。"""
    return state.index(BLANK)

def row_col(index: int) -> tuple[int, int]:
    """下标转 (行, 列)。"""
    return divmod(index, SIZE)
