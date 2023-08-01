def is_valid(grid,row,col,num):

    # input check
    for y in range(9):
        if grid[row][y]==num:
            return False

    for x in range(9):
        if grid[x][col]==num:
            return False

    box_row=row-row%3
    box_col=col-col%3

    for x in range(3):
        for y in range(3):
            if grid[box_row+x][box_col+y]==num:
                return False

    return True

def solution(grid,row,col):

    if col == 9:
        if row == 8:
            return True  # Sudoku Solved
        row+=1
        col=0

    if grid[row][col]>0:
        return solution(grid,row,col+1)

    for num in range(1,10):
        if is_valid(grid,row,col,num):
            grid[row][col]=num

            if solution(grid,row,col+1):
                return True

        grid[row][col]=0

    return False  # NO SOLUTION FOR THE GIVEN SUDOKU!!!

def Solve(grid):

    if solution(grid,0,0):
        print("Solution: ")
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
            print()
    else:
        print("No Possible Solution For the give Sudoku!!!")




# Testing:

#give your own Sudoku to solve:
Sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

Solve(Sudoku)