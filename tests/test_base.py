"""base.py 的单元测试"""

import dataclasses

import pytest

from puzzle_core.constants import GOAL, RIGHT
from puzzle_core.search.base import Node, SearchResult, reconstruct_path
from puzzle_core.state import parse_state

START = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    
def test_node_defaults():
    """
    测试 Node 的默认属性值是否正确
    """
    node = Node(GOAL)
    assert node.parent is None
    assert node.action is None
    assert node.depth == 0
    assert node.g == 0
    assert node.h == 0
    assert node.f == 0

def test_node_f_is_g_plus_h():
    """测试 @property 装饰的 f 属性计算逻辑是否正确"""
    node = Node(GOAL, depth=3, g=5, h=7)
    assert node.f == 12

def test_node_is_frozen():
    """测试 Node 是否是不可变的（frozen dataclass）"""
    node = Node(GOAL)
    with pytest.raises(dataclasses.FrozenInstanceError):
        node.g = 10

def test_reconstruct_path_single_node():
    """
    测试 reconstruct_path 在只有一个节点（根节点）的情况下的行为
    """
    states, actions = reconstruct_path(Node(GOAL))
    assert states == [GOAL]
    assert actions == []

def test_reconstruct_path_walks_back_to_root():
    """
    测试多步移动的路径还原是否正确

    1. 核心逻辑：
        1. 回溯正确且顺序正确
        2. 动作序列比状态序列少一个元素
    """ 
    root = Node(START)
    mid = Node(parse_state("1 2 3 4 5 6 7 0 8"),parent = root, action = RIGHT,depth = 1, g = 1, h = 1)
    goal = Node(GOAL, parent = mid, action = RIGHT, depth = 2, g = 2, h = 0)

    states, actions = reconstruct_path(goal)

    assert states == [START, mid.state, GOAL]
    assert actions == [RIGHT, RIGHT]

def test_search_result_defaults_are_independent():
    """
    测试 SearchResult 的默认属性值是否正确，且每个实例的默认列表是独立的
    """
    result1 = SearchResult(algorithm="BFS", found=False)
    result2 = SearchResult(algorithm="BFS", found=False)
    result1.path.append(GOAL)
    assert result1.path == [GOAL]
    assert result2.path == []
    assert result2.actions == []
    assert result2.expanded == 0
