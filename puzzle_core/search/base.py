"""
搜索算法的基础数据结构与通用接口

本模块定义了所有搜索算法（如 BFS、A* 等）共享的底层组件：
    1. Node: 搜索树的节点，记录了状态、代价以及父子关系，用于构建搜索树
    2. SearchResult: 统一了所有算法的输出格式，方便上层调用（如 UI 或测试脚本）

设计目的：将数据结构与具体算法解耦，保证不同算法之间接口高度统一
"""

from dataclasses import dataclass, field

from ..constants import Action
from ..state import State

@dataclass(frozen=True, slots=True)
class Node:
    """
    搜索树里的一个节点
    
    1. Attributes:
        1. state: 当前拼图的状态（如 (1, 2, 3, 4, 5, 6, 7, 8, 0)）
        2. parent: 父节点引用，用于从终点向起点逆向回溯完整路径。根节点为 None
        3. action: 从父节点走到当前节点所执行的动作（如 'UP'），根节点为 None
        4. depth: 当前节点在搜索树中的深度（即从根节点走到这里的步数）
        5. g: 从根节点（起点）到当前节点的实际已花代价（通常 g == depth）
        6. h: 从当前节点到目标节点的启发式预估代价（如曼哈顿距离）
    """

    state: State
    parent: "Node|None" = None
    action: Action|None = None
    depth: int = 0
    g: int = 0
    h: int = 0

    @property
    def f(self) -> int:
        """
        当前节点的综合评估代价 f = g + h

        A* 算法的核心：算法会将节点放入优先队列，并根据 f 值从小到大排序
        f 值越小，说明这条路（已走代价 + 预估剩余代价）越有希望，越优先探索
        """
        return self.g + self.h

@dataclass
class SearchResult:
    """
    一次搜索的完整结果。所有算法（BFS, A*, IDA* 等）都统一返回这个结构。

    1. Attributes:
        1. algorithm (str): 使用的搜索算法名称（如 'BFS', 'A*'）
        2. found (bool): 是否成功找到了从起点到终点的路径
        3. path (list[State]): 从起点到终点的状态序列，如果没找到则为空
        4. actions (list[Action]): 对应的移动动作序列（如 ['UP', 'DOWN']）
        5. expanded (int): 实际从优先队列/栈中取出并展开的节点数量
        6. generated (int): 搜索过程中总共生成的子节点数量（含重复状态）
        7. peak_frontier (int): Frontier（边界/开启列表）在搜索过程中的最大容量
        8. elapsed_ms (float): 搜索算法运行的总耗时（毫秒）
    """

    algorithm: str
    found: bool
    path: list[State] = field(default_factory=list)
    actions: list[Action] = field(default_factory=list)
    expanded: int = 0
    generated: int = 0
    peak_frontier: int = 0
    elapsed_ms: float = 0.0


def reconstruct_path(node: Node) -> tuple[list[State], list[Action]]:
    """
    从终点节点逆向回溯到起点，重建完整的状态路径和动作序列。

    1. Args:
        1. node (Node): 搜索树中的终点节点

    2. Returns:
        1. tuple[list[State], list[Action]]: 
            - 状态路径列表，从起点到终点
            - 动作序列列表，对应每一步的移动动作
    """
    states: list[State] = []
    actions: list[Action] = []
    current: Node|None = node
    while current is not None:
        states.append(current.state)
        if current.action is not None:
            actions.append(current.action)
        current = current.parent
    states.reverse()
    actions.reverse()
    return states, actions