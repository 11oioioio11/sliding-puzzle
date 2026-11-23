"""全局常量：尺寸、空格、目标态、动作名。不 import 项目内的其他模块，避免循环引用。"""

from typing import Literal

type Action = Literal["UP", "DOWN", "LEFT", "RIGHT"]

SIZE = 3  # 拼图尺寸
CELLS = SIZE * SIZE  # 拼图格子数
BLANK = 0  # 空格的值
GOAL: tuple[int, ...] = tuple(range(1, CELLS)) + (BLANK,)  # 目标态

UP: Action = "UP"
DOWN: Action = "DOWN"
LEFT: Action = "LEFT"
RIGHT: Action = "RIGHT"