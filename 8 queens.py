# 八皇后问题
import copy
board_size = 8
board = [[-1 for _ in range(board_size)] for _ in range(board_size)]

# 刷新棋盘剩余行不可取位置
def revise(board,row,col):
    board[row][0:col] = [0]*col
    board[row][col+1:board_size] = [0]*(board_size-(col+1))
    for i in board[row+1:]:
        i[col] = 0

    for i in range(row+1,board_size):
        if col+i-row < board_size:
            board[i][(col+i-row)]=0
        if col+row-i >= 0:
            board[i][(col+row-i)]=0

feasible_solution = []
def deploy(board_test,row):
    if board_test[row] == [0]*board_size:
        return
    for col in range(board_size):
        if board_test[row][col] == -1:
            board_new = copy.deepcopy(board_test)
            board_new[row][col] = 1
            if row == board_size-1:
                feasible_solution.append(board_new)
                continue
            revise(board_new,row,col)
            deploy(board_new, row+1)

deploy(board, 0)