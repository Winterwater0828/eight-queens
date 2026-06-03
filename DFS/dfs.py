def DFS_eight_queens():
    all_solutions = []
    # 递归函数：尝试在当前棋盘上放置下一个皇后
    # current_board: 列表，存储已放置皇后的列位置
    # current_board[i] = 第i行皇后所在的列
    def place_queen(current_board):
        # 终止：如果已经放置了8个皇后，找到一个完整解
        if len(current_board) == 8:
            all_solutions.append(current_board.copy())
            return       
        # 当前要放置的行号（从0开始）
        current_row = len(current_board)     
        # 尝试在当前行的每一列放置皇后
        for column in range(8):
            is_safe = True          
            # 检查与之前已放置的所有皇后是否有冲突
            for previous_row in range(len(current_board)):
                previous_column = current_board[previous_row]
                # 检查1：是否在同一列
                if previous_column == column:
                    is_safe = False
                    break       
                # 检查2：是否在同一对角线上
                # 对角线检查：行差 = 列差的绝对值
                row_difference = abs(current_row - previous_row)
                col_difference = abs(column - previous_column)
                if row_difference == col_difference:
                    is_safe = False
                    break
            
            # 如果当前位置安全
            if is_safe:
                # 做出选择：放置皇后
                current_board.append(column)
                # 递归调用：放置下一个皇后
                place_queen(current_board)
                # 撤销选择：回溯，移除刚放置的皇后
                current_board.pop()

    # 从空棋盘开始搜索
    place_queen([])
    
    # 输出结果
    print(f"找到 {len(all_solutions)} 个解决方案")
    
    # 显示前5个解决方案
    for i, solution in enumerate(all_solutions[:5], 1):
        print(f"方案 {i}: {solution}")
    
    return all_solutions

solutions = DFS_eight_queens()