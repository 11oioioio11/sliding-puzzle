"""
1. 拼图游戏的核心常量与基础类型定义。
2. 本模块是项目的“基石”模块，严格禁止导入项目内的其他模块，以防范循环引用。
3. 所有搜索算法、状态工具、业务层均可安全导入本模块。
"""

from typing import Literal

# 动作规范（仅允许这四个字面量）
type Action = Literal["UP", "DOWN", "LEFT", "RIGHT"]

SIZE = 3  # 拼图尺寸
CELLS = SIZE * SIZE  # 拼图格子数
BLANK = 0  # 空格的值

# 目标态：动态生成。对于 SIZE=3，结果是 (1, 2, 3, 4, 5, 6, 7, 8, 0)
GOAL: tuple[int, ...] = tuple(range(1, CELLS)) + (BLANK,)  # 目标态

# 动作常量（配合类型注解，避免手敲字符串时拼写错误）
UP: Action = "UP"
DOWN: Action = "DOWN"
LEFT: Action = "LEFT"
RIGHT: Action = "RIGHT"