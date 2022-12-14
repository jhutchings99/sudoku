import random
#this is the algorythmn inplemeted here
# 0 0 0 | 1 0 0 | 0 0 0 | #random placement if == 0
# 0 0 0 | x x x | 0 0 0 | # place 'x' on next row where it cant be if == 0
# 0 0 0 | x x x | 0 0 0 |
#________________________
# 0 0 0 | 1 0 0 | 0 0 0 |
# 0 0 0 | x x x | 0 1 0 | #random placement if == 0
# 0 0 0 | x x x | x x x | #place 'x' on next row where it cant be if ==0
                             #replace 'x''s at end 0's

def printGrid(grid):
    for row in range(9):
        print()
        for column in range(9):
            print(grid[row][column], end=" ")

def createGrid():
    grid = []
    for row in range(9):
        grid.append([])
        for column in range(9):
            grid[row].append(0)
    return grid

def placeInRow(grid, y, columns, num):
    x = 'x'
    for column in columns:
        if grid[y][column] == 0:
            x = column
            break
    if x == 'x':
        raise Exception("x should not == 'x'")

    grid[y][x] = num
    if y+1 < 9:
        checkNextRow(grid, y+1,x)
    else:
        replaceMinusOne(grid)
    return

def checkNextRow(grid, y, x):
    i=0
    while (y+i) < 9: #this elimiates the column from being chosen again
        if grid[y+i][x] == 0:
            grid[y+i][x] = 'x'
        i+=1
    position = x % 3
    if (y-1) % 3 == 0:# if it is in the first row of the box eliminate the other options in the box
        if position == 0:
            if grid[y][x+1] == 0:
                grid[y][x+1] = 'x'
            if grid[y][x+2] == 0:
                grid[y][x+2] = 'x'
            if grid[y+1][x+1] == 0:
                grid[y+1][x+1] = 'x'
            if grid[y+1][x+2] == 0:
                grid[y+1][x+2] = 'x'
        elif position == 1:
            if grid[y][x+1] == 0:
                grid[y][x+1] = 'x'
            if grid[y][x-1] == 0:
                grid[y][x-1] = 'x'
            if grid[y+1][x+1] == 0:
                grid[y+1][x+1] = 'x'
            if grid[y+1][x-1] == 0:
                grid[y+1][x-1] = 'x'
        else:
            if grid[y][x-2] == 0:
                grid[y][x-2] = 'x'
            if grid[y][x-1] == 0:
                grid[y][x-1] = 'x'
            if grid[y+1][x-2] == 0:
                grid[y+1][x-2] = 'x'
            if grid[y+1][x-1] == 0:
                grid[y+1][x-1] = 'x'
    if (y-1) % 3 == 1: #if it is the second row we only need to eliminate the next row for the box 
        if position == 0:
            if grid[y][x+1] == 0:
                grid[y][x+1] = 'x'
            if grid[y][x+2] == 0:
                grid[y][x+2] = 'x'
        elif position == 1:
            if grid[y][x+1] == 0:
                grid[y][x+1] = 'x'
            if grid[y][x-1] == 0:
                grid[y][x-1] = 'x'
        else:
            if grid[y][x-2] == 0:
                grid[y][x-2] = 'x'
            if grid[y][x-1] == 0:
                grid[y][x-1] = 'x'
    return

def replaceMinusOne(grid):
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 'x':
                grid[row][column] = 0
    return
            

def main():
    grid = createGrid()
    column = [0,1,2,3,4,5,6,7,8]
    for num in range(1,10):
        for row in range(9):
            random.shuffle(column)
            placeInRow(grid, row, column, num)
            print("_____")
            printGrid(grid)
            print()
            input("")
    printGrid(grid)
    print()
    return

if __name__ == '__main__':
    main()
