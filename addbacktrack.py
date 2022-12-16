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
count = 0
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

def calculateGridNumber(row, gridnumber):
    if gridnumber == -1:
        gridnumber = row-1
    else:
        gridnumber -= 1
    return gridnumber

def backtrack(grid, grids, gridnumber, columns, number, y):
    if grids[gridnumber] == False:
        print("starting over grids are empty")
        return False #just start over 
    grid = grids[gridnumber]
    row = -1
    column = -1
    for c in range(len(grid[gridnumber])): # loop through each column in row
        if grid[gridnumber][c] == number:
            # print("grid[r][c]=",grid[gridnumber][c],"number=",number, "gridnumber=",gridnumber)
            row = gridnumber
            column = c
            break
    if row == -1 or column == -1:
        raise Exception("Couldnt find number in grid")
    grid[row][column] = 'x'
    replaceSpecialX(grid, number)
    grid[row][column] = 'x'
    backtrackNumber = y - gridnumber+1 
    # print("backtrackNumber =",backtrackNumber)
    for i in range(backtrackNumber):
        x = 'x'
        for c in range(len(columns)):
            if grid[row+i][columns[c]] == 0:
                x = columns[c]
                break
        if x == 'x':
            # print("backTracking again.... ")
            # replaceSpecialX(grid, number)
            # gridnumber = calculateGridNumber(row-i, gridnumber)
            # print("x=",x, "row=",row-i)
            # b = backtrack(grid , grids, gridnumber, columns,number, row-i)
            # for trys in range(1):
            #     for c in range(len(columns)):
            #         if grid[row-i][columns[c]] == 0:
            #             x = column[c]
            #             break
            #     if x != 'x':
            #         break
            #     replaceSpecialX(grid,number)
            #     gridnumber = calculateGridNumber(row-i, gridnumber)
            #     print("again... x=",x,"row=",row-i)
            #     b = backtrack(grid, grids, gridnumber, columns, number, row-i)
            # if x == 'x':
            # print("backtrack failed starting over...")
            global count
            count+=1
            return False
            # if b == False:
            #     return b
        y = row+i
        grid[y][x] = number
        if y+1 < 9:
            checkNextRow(grid,y+1,x)
        else:
            # print("backtracked successfully to end of list")
            return True #backtracked successfully to end of list end
        # print("------BackTrackGrid------")
        # printGrid(grid)
        # print("---")
        # input()
        grids.append(grid)
    # print("backtracked successfully to end of backtrack number")
    return True #backtraced successfully to backtrack number




def placeInRow(grid, y, columns, num, grids, gridnumber):
    x = 'x'
    for column in range(len(columns)):
        if grid[y][columns[column]] == 0:
            x = columns[column]
            break
    if x == 'x':
        # raise Exception("x should not == 'x'")
        # print("backTracking .... ")
        gridnumber = calculateGridNumber(y, gridnumber)
        b = backtrack(grid , grids, gridnumber, columns,num, y)
        return b
        #Back track here some how
    
    grid[y][x] = num
    grids.append(grid)
    if y+1 < 9:
        checkNextRow(grid, y+1,x)
    else:
        replaceX(grid)
    return True

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

def replaceX(grid):
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 'x':
                grid[row][column] = 0
    return

def replaceSpecialX(grid, num):
    keepXs =[]
    for row in range(9):
        for column in range(9):
            if grid[row][column] == num:
                keepXs.append(column)
            if column in keepXs:
                continue;
            if grid[row][column] == 'x':
                grid[row][column] = 0
    return

            

def main():
    grid = createGrid()
    column = [0,1,2,3,4,5,6,7,8]
    for num in range(1,10):
        grids = [False]
        gridnumber = -1
        for row in range(9):
            random.shuffle(column)
            x = placeInRow(grid, row, column, num, grids, gridnumber)
            if x == False:
                main()
                return
            # print("_____")
            # printGrid(grid)
            # print()
            # input("")
    printGrid(grid)
    print()
    global count
    print("restarted =",count,"times")
    print()
    return

#when ran 10 times, got restarts ranging from 9 - 118 with an adverage of 53.6 times
# if it works it works lol


if __name__ == '__main__':
    main()
