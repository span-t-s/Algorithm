import sys
from io import StringIO

sys.stdin = StringIO("""5
.X..X
..X.X
XX..X
..X.X
X.X.X
0
""")

def findmaximum(board:list[list[str]])->int:
    row = len(board)
    col = len(board[0])
    ans = 0

    # 逐行从左到右遍历
    for i in range(row):
        for j in range(col):
            if board[i][j] not in('X','0'):
                # 贪心算法且能保证为最优解：对所在（部分）行中每个点，比较点往正下方所覆盖的范围点数
                m,n = i,j
                freecol = []
                while n < col and board[i][n]!= 'X':
                    col_m = 0
                    while m < row and board[m][n] != 'X':  
                        col_m += 1
                        m += 1
                    freecol.append(col_m)
                    n += 1
                selected_col = j+freecol.index(min(freecol))

                # 将选择的点(i,seleted_col)所在十字射程设为‘0’（代表不可选）
                for n in range(j,col):
                    if board[i][n] != 'X':
                        board[i][n] = '0'
                    else:break
                for m in range(i,row):
                    if board[m][selected_col] != 'X':
                        board[m][selected_col] = '0'
                    else:break
                ans += 1

    return ans


while (n:=input()) != '0':
    board = []
    for _ in range(int(n)):
        board.append(list(input()))

    print(findmaximum(board))