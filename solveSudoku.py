#解数独
def solveSudoku(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    empty = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                empty.append([i,j])
    def isvalid(i,j,num):
        for x in board[i]:
            if x == str(num):
                return False
            
        for row in board:
            y = row[j]
            if y == str(num):
                return False           
        xmin = i//3*3
        ymin = j//3*3
        for x in range(xmin,xmin+3):
            for y in range(ymin,ymin+3):
                if board[x][y] == str(num):
                    return False
        return True
    
    def fillnext(k):
        if k == len(empty):
            return True
        for i,j in empty[k:]:
            for num in range(1,10):
                if isvalid(i,j,num):
                    board[i][j] = str(num)
                    if fillnext(k+1):
                        return True
            board[i][j] = '.'
            return
    fillnext(0)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
print(board)