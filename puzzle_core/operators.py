def get_neighbors(state):
    """
    获取当前状态下的所有可能的下一个状态
    """
    neighbors = []
    zero_idx = state.index(0)  # 找到空格的位置

    row = zero_idx // 3
    col = zero_idx % 3

    if row > 0:  # 上
        new_state = list(state)
        new_state[zero_idx], new_state[zero_idx - 3] = new_state[zero_idx - 3], new_state[zero_idx]
        neighbors.append(('UP', tuple(new_state)))
    if row < 2:  # 下
        new_state = list(state)
        new_state[zero_idx], new_state[zero_idx + 3] = new_state[zero_idx + 3], new_state[zero_idx]
        neighbors.append(('DOWN', tuple(new_state)))
    if col > 0:  # 左
        new_state = list(state)
        new_state[zero_idx], new_state[zero_idx - 1] = new_state[zero_idx - 1], new_state[zero_idx]
        neighbors.append(('LEFT', tuple(new_state)))
    if col < 2:  # 右
        new_state = list(state)
        new_state[zero_idx], new_state[zero_idx + 1] = new_state[zero_idx + 1], new_state[zero_idx]
        neighbors.append(('RIGHT', tuple(new_state)))

    return neighbors