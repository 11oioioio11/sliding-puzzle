# sliding-puzzle

八数码（8-puzzle）求解器：状态空间搜索与元启发式算法练习。

> 8-puzzle solver: BFS / DFS / best-first + metaheuristics

## 快速开始

**环境要求**：Python 3.12+（代码使用了 `type` 语句），运行时不依赖任何第三方包。

```bash
git clone https://github.com/11oioioio11/sliding-puzzle.git
cd sliding-puzzle
python main.py
```

输出：

```text
初始状态:
----------------
|  1 |  6 |  2 |
|  5 |  7 |  3 |
|    |  4 |  8 |
----------------

========================================
算法：bfs
是否可解：True
步数：10
动作：RIGHT -> UP -> UP -> RIGHT -> DOWN -> LEFT -> LEFT -> DOWN -> RIGHT -> RIGHT

如果print_result参数trace为True，会逐步打印每一步的棋盘，最后一行是扩展数、生成数、队列峰值和耗时
```

### 运行测试

```bash
# 建一个独立环境（conda 或 venv 任选）
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

pip install -r requirements-dev.txt
python -m pytest -q
```

## 项目结构

```text
sliding-puzzle/
├─ main.py                  # 命令行入口
├─ puzzle_core/
│  ├─ constants.py          # 尺寸、空格、目标态、动作名
│  ├─ state.py              # 解析、校验、目标判定、可解性、坐标换算
│  ├─ operators.py          # 邻域算子：空格四方向移动
│  ├─ board_utils.py        # 终端打印
│  ├─ heuristics.py         # 启发式函数（待实现）
│  └─ search/
│     ├─ __init__.py
│     ├─ base.py            # Node、SearchResult、路径还原
│     └─ bfs.py             # 广度优先搜索
├─ tests/
│  ├─ test_state.py
│  ├─ test_base.py
│  └─ test_bfs.py
├─ requirements-dev.txt     # 仅测试依赖
├─ README.md
├─ LICENSE
└─ 工作记录.md
```

## 设计说明

- 状态是长度 9 的不可变元组，空格记为 `0`，可以直接作为 `set` / `dict` 的键，便于判重。
- `puzzle_core` 是领域层（状态、算子、启发式），`puzzle_core/search` 是搜索层。算法只依赖 `Node` 和 `SearchResult` 两个接口，输出格式统一，方便横向对比。
- 可解性用逆序数奇偶判定：去掉空格后，起点与目标的逆序数奇偶相同才可达（仅对奇数阶成立）。

## 路线图

- [x] 状态表示、解析与合法性校验
- [x] 目标判定与可解性判定（逆序数）
- [x] 邻域算子（空格四方向移动）
- [x] 搜索结点 `Node`、结果 `SearchResult`、路径还原
- [x] 广度优先搜索（BFS）
- [ ] 深度优先搜索（DFS）
- [ ] 最佳优先搜索（GBFS / A*）
- [ ] 启发式函数：错位数、曼哈顿距离
- [ ] 元启发式：爬山、模拟退火
- [ ] 命令行参数与算法对比表

## 许可证

MIT，见 [LICENSE](LICENSE)。