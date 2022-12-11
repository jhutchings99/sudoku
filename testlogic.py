import random
def testprintGrid():
    for row in range(9):
        print()
        for column in range(9):
            # print("0", end=" ")
            if row < 3:
                if column < 3:
                    print("1", end=" ")
                elif column < 6:
                    print("2", end=" ")
                else:
                    print("3", end=" ")
            elif row < 6:
                if column < 3:
                    print("4", end=" ")
                elif column < 6:
                    print("5", end=" ")
                else:
                    print("6", end=" ")
            elif row < 9:
                if column < 3:
                    print("7", end=" ")
                elif column < 6:
                    print("8", end=" ")
                else:
                    print("9", end=" ")
            else:
                print("("+str(row)+","+str(column)+")", end=" ")
# testprintGrid()

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
# printGrid(createGrid())
            

def placeNumber(grid, num):
    row = [[0,1,2],[3,4,5],[6,7,8]]
    column = [[0,1,2],[3,4,5],[6,7,8]]
    for r in range(3):
        for c in range(3):
            x = random.choice(row[r])
            y = random.choice(column[c])
            placeGrid(grid, num,x,y, row[r], column[c])
            row[r].remove(x)
            column[c].remove(y)
    # printGrid(grid)

def placeGrid(grid, num, x, y, row, column):
    if grid[y][x] != 0:
        for i in range(len(row)):
            for j in range(len(column)):
                x = row[i]
                y = column[j]
                if grid[y][x] == 0:
                    grid[y][x] = num
                    return
    grid[y][x] = num
    return

# placeNumber(createGrid(), 1)

def main():
    grid = createGrid() # still getting 0s :(
    for i in range(9):
        placeNumber(grid,(i+1))
    printGrid(grid)

main()
