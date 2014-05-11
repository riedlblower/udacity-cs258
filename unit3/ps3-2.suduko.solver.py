
# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
# hard = [[1,0,0,0,0,7,0,9,0],
#         [0,3,0,0,2,0,0,0,8],
#         [0,0,9,6,0,0,5,0,0],
#         [0,0,5,3,0,0,9,0,0],
#         [0,1,0,0,8,0,0,0,2],
#         [6,0,0,0,0,4,0,0,0],
#         [3,0,0,0,0,0,0,1,0],
#         [0,4,0,0,0,0,0,0,7],
#         [0,0,7,0,0,0,3,0,0]]

def solve_sudoku (grid):
    res = check_sudoku(grid)
    if res == False or res == None:
        return res
    zero_positions = find_zeroes(grid)
    if len(zero_positions) == 0:
        return grid
    return finish_grid(grid, zero_positions)
    
def find_zeroes(grid):
    zeroes = []
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                zeroes.append((i,j))
    return zeroes

def finish_grid(grid, zero_positions):
    position = zero_positions[0]
    for i in range(1, 10):  # let's go with 1 to 9 in first zero position
        grid[position[0]][position[1]] = i
        if check_sudoku(grid) == True:    #if the grid is now valid 
            if len(zero_positions) == 1:   #if the grid is full of non zero numbers 
                return grid               #then exit
            result = finish_grid(grid, zero_positions[1:]) #let's try the next zero position
            if result != False:            #exit if all is good
                return result
    grid[position[0]][position[1]] = 0   #put the zero back into its position in grid
    return False                        #exit with False

     
def check_ill_formed(grid):
    index = 0
    for row in grid:
        if len(row) != 9:
            return True   # bad grid if not 9 elements in row
        for cell in row:
            if type(cell) != int or cell > 9 or cell < 0:
                return True
        index = index + 1    
    if index != 9:
        return True   # bad grid if not 9 rows
    return False 
 
def check_valid_sequence(list1):
    for cell in list1:
        if cell != 0:
            if list1.count(cell) != 1:
                return False  
    return True
            
def get_list(grid,x,y):
    ystart = y
    list1 = []
    for i in range (0,3):
        for j in range (0,3):
            list1.append(grid[x][y])
            y = y + 1
        y = ystart
        x = x + 1    
    return list1
 
def check_valid_grid(grid):
    column = []
    square_list = []
    for row in grid:    # let's check rows first for repeated non zero digits
        if check_valid_sequence(row) == False:
            return False
    for i in range (0,9):   #let's check columns for repeated non zero digits
        for j in range (0,9):
            column.append(grid[j][i])
        if check_valid_sequence(column) == False:
            return False
        column = []
    for i in range (0,3):     #let's check squares for repeated non zero digits
        for j in range (0,3):
            square_list = get_list(grid,i*3,j*3)
            if check_valid_sequence(square_list) == False:
                return False
            j = j + 1
        j = 0
        i = i + 1
    return True
       
def check_sudoku(grid):
    if (check_ill_formed(grid)):
        return None    # grid was ill_formed
    if (check_valid_grid(grid)):
        return True     # grid was valid
    else:
        return False    # grid was invalid
  
print solve_sudoku(ill_formed)
print solve_sudoku(valid)
print solve_sudoku(invalid)
print solve_sudoku(easy)
#print solve_sudoku(hard)
    
