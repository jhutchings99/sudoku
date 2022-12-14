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
    print("placing",num,"into",grid[y][x], end="...")
    if grid[y][x] != 0:
        for i in range(len(row)):
            for j in range(len(column)):
                x = row[i]
                y = column[j]
                print("placing",num,"into",grid[y][x], end="...")
                if grid[y][x] == 0:
                    print("Success")
                    grid[y][x] = num
                    return
    if grid[y][x] != 0:
        print("Failed")
        print(row)
        print(column)
        return
    print("Succsess")
    grid[y][x] = num
    return

# placeNumber(createGrid(), 1)

# def main():
#     grid = createGrid() # still getting 0s :(
#     for i in range(9):
#         placeNumber(grid,(i+1))
#     print()
#     print(grid)

#goto here 
def placeRow(grid, grid2, row):
    R = [1,2,3,4,5,6,7,8,9]
    random.shuffle(R)
    c = -1
    while True:
        c+=1
        if c > 8:
            c =0
        canbreak = False
        if R[c] not in grid2[c]: # this is whatu I have been messing with row and c
            print(R[c],"(",c,")","not in",grid2[c],"(",c,")")
            canbreak = True
            if c % 3 == 1: #check box row 2
                if checkRow(c,grid,row,1,R) == False:
                    if c+1 > 8:
                        random.shuffle(R)
                    else:
                        R[c], R[c+1] = R[c+1], R[c] #maybe do a better more complex swap later
                    continue
            elif c % 3 == 2:
                if checkRow(c,grid,row,1,R) == False:
                    if c+1 > 8:
                        random.shuffle(R)
                    else:
                        R[c], R[c+1] = R[c+1], R[c] #maybe do a better more complex swap later
                    continue
                if checkRow(c,grid,row,2,R) == False:
                    if c+1 > 8:
                        random.shuffle(R)
                    else:
                        R[c], R[c+1] = R[c+1], R[c] #maybe do a better more complex swap later
                    continue
            grid2[c].append(R[c])
        # print(R, c)
            print(len(grid2[c]),c+1)
            if c>=8 and canbreak:
                break
    for i in range(9):
        grid[row][i] = R[i]
    return


def checkRow( c, grid , row , above, R ):
    if c % 3 == 0: #check box column 1
        if grid[row-above][c+1] != R[c]: #comparing row 1 with it
            if grid[row-above][c+2] != R[c]: #comparing row 1 with it middle and right
                #this row is good
                #+ ? ?
                #X + +
                #- - -
                # where + is good by default
                # where ? is check this
                # where X is what to check with
                # where - is not rendered yet
                return True
    if c % 3 == 1: #check box column 2
        if grid[row-above][c-1] != R[c]: #compare left corner with it
            if grid[row-above][c+1] != R[c]:
                #? + ?
                #+ X +
                #- - -
                return True
    else: #check box colun 3
        if grid[row-above][c-1] != R[c]: #compare upper middle with it
            if grid[row-above][c-2] != R[c]:
                #? ? +
                #+ + X
                #- - -
                return True
    return False

def main():
    grid = createGrid()
    grid2 = [[],[],[],[],[],[],[],[],[]]
    for i in range(2):
        placeRow(grid, grid2, i)
    printGrid(grid)
    print()# the checks dont work
    print(grid2)
    print()

main()

######

#new method - > create a premade sudoku board then mix it up
# or maybe use this method
# 1 0 0 | 0 0 0 | 0 0 0 |
# 0 0 0 | 1 0 0 | 0 0 0 |
# 0 0 0 | 0 0 0 | 1 0 0 |

# 0 1 0 | 0 0 0 | 0 0 0 |
# 0 0 0 | 0 1 0 | 0 0 0 |
# 0 0 0 | 0 0 0 | 0 1 0 |

# 0 0 1 | 0 0 0 | 0 0 0 |
# 0 0 0 | 0 1 0 | 0 0 0 |
# 0 0 0 | 0 0 0 | 0 0 1 |
#________________________

# 1 2 0 | 0 0 0 | 0 0 0 |
# 0 0 0 | 1 2 0 | 0 0 0 |
# 0 0 0 | 0 0 0 | 1 2 0 |

# 0 1 2 | 0 0 0 | 0 0 0 |
# 0 0 0 | 0 1 2 | 0 0 0 |
# 0 0 0 | 0 0 0 | 0 1 2 |

# 2 0 1 | 0 0 0 | 0 0 0 |
# 0 0 0 | 2 1 0 | 0 0 0 |
# 0 0 0 | 0 0 0 | 2 0 1 |
#________________________

# 1 2 3 | 0 0 0 | 0 0 0 |
# 0 0 0 | 1 2 3 | 0 0 0 |
# 0 0 0 | 0 0 0 | 1 2 3 |

# 3 1 2 | 0 0 0 | 0 0 0 |
# 0 0 0 | 3 1 2 | 0 0 0 |
# 0 0 0 | 0 0 0 | 3 1 2 |

# 2 3 1 | 0 0 0 | 0 0 0 |
# 0 0 0 | 2 1 3 | 0 0 0 |
# 0 0 0 | 0 0 0 | 2 3 1 |
#________________________

# 1 2 3 | 0 0 0 | 0 0 4 |
# 4 0 0 | 1 2 3 | 0 0 0 |
# 0 0 0 | 4 0 0 | 1 2 3 |

# 3 1 2 | 0 0 0 | 4 0 0 |
# 0 4 0 | 3 1 2 | 0 0 0 |
# 0 0 0 | 0 4 0 | 3 1 2 |

# 2 3 1 | 0 0 0 | 0 4 0 |
# 0 0 4 | 2 1 3 | 0 0 0 |
# 0 0 0 | 0 4 0 | 2 3 1 |
#________________________

# 1 2 3 | 0 0 0 | 5 0 4 |
# 4 5 0 | 1 2 3 | 0 0 0 |
# 0 0 0 | 4 5 0 | 1 2 3 |

# 3 1 2 | 0 0 0 | 4 5 0 |
# 0 4 5 | 3 1 2 | 0 0 0 |
# 0 0 0 | 0 4 5 | 3 1 2 |

# 2 3 1 | 0 0 0 | 0 4 5 |
# 5 0 4 | 2 1 3 | 0 0 0 |
# 0 0 0 | 5 4 0 | 2 3 1 |
#________________________

# 1 2 3 | 0 0 0 | 5 6 4 |
# 4 5 6 | 1 2 3 | 0 0 0 |
# 0 0 0 | 4 5 6 | 1 2 3 |

# 3 1 2 | 0 0 0 | 4 5 6 |
# 6 4 5 | 3 1 2 | 0 0 0 |
# 0 0 0 | 6 4 5 | 3 1 2 |

# 2 3 1 | 0 0 0 | 6 4 5 |
# 5 6 4 | 2 1 3 | 0 0 0 |
# 0 0 0 | 5 4 6 | 2 3 1 |
#________________________

# 1 2 3 | 0 7 0 | 5 6 4 |
# 4 5 6 | 1 2 3 | 0 0 7 |
# 7 0 0 | 4 5 6 | 1 2 3 |

# 3 1 2 | 7 0 0 | 4 5 6 |
# 6 4 5 | 3 1 2 | 7 0 0 |
# 0 7 0 | 6 4 5 | 3 1 2 |

# 2 3 1 | 0 7 0 | 6 4 5 |
# 5 6 4 | 2 1 3 | 0 7 0 |
# 0 0 7 | 5 4 6 | 2 3 1 |
#________________________

# 1 2 3 | 8 7 0 | 5 6 4 |
# 4 5 6 | 1 2 3 | 8 0 7 |
# 7 8 0 | 4 5 6 | 1 2 3 |

# 3 1 2 | 7 8 0 | 4 5 6 |
# 6 4 5 | 3 1 2 | 7 8 0 |
# 0 7 8 | 6 4 5 | 3 1 2 |

# 2 3 1 | 0 7 8 | 6 4 5 |
# 5 6 4 | 2 1 3 | 0 7 8 |
# 8 0 7 | 5 4 6 | 2 3 1 |
#________________________

# 1 2 3 | 8 7 9 | 5 6 4 |
# 4 5 6 | 1 2 3 | 8 9 7 |
# 7 8 9 | 4 5 6 | 1 2 3 |

# 3 1 2 | 7 8 9 | 4 5 6 |
# 6 4 5 | 3 1 2 | 7 8 9 |
# 9 7 8 | 6 4 5 | 3 1 2 |

# 2 3 1 | 9 7 8 | 6 4 5 |
# 5 6 4 | 2 1 3 | 9 7 8 |
# 8 9 7 | 5 4 6 | 2 3 1 |
#________________________

# 1 2 3 | 8 7 9 | 5 6 4 |
# 4 5 6 | 1 2 3 | 8 9 7 |
# 7 8 9 | 4 5 6 | 1 2 3 |
#________________________
# 3 1 2 | 7 8 9 | 4 5 6 |
# 6 4 5 | 3 1 2 | 7 8 9 |
# 9 7 8 | 6 4 5 | 3 1 2 |
#________________________
# 2 3 1 | 9 7 8 | 6 4 5 |
# 5 6 4 | 2 1 3 | 9 7 8 |
# 8 9 7 | 5 4 6 | 2 3 1 |
#________________________

# PREMADE-Grid = [[1,2,3,8,7,9,5,6,4],[,4,5,6,1,2,3,8,9,7],[7... 
