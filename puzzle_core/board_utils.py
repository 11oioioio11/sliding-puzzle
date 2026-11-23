def print_state(state):
    """
    辅助函数，将一维元组打印成3×3的矩阵
    """
    print("----------------")
    for i in range(0, 9, 3):
        row = state[i:i+3]
        # 把 0 替换成空白字符，方便查看
        row_str = [str(x) if x != 0 else ' ' for x in row]
        print(f"| {row_str[0]} | {row_str[1]} | {row_str[2]} |")
    print("----------------\n")