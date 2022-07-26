# Week 2 Problem 8 - "Grid Challenge"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/

# inputs:
# grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

def gridChallenge(grid):
    gl = len(grid)
    sgrid = True
    for i in range(gl):
        grid[i] = sorted(grid[i])
    
    gil = len(grid[0])
    for i in range(gil):
        for j in range(1,gl):
            if grid[j-1][i] > grid[j][i]:
                sgrid = False
                
    return "YES" if sgrid else "NO"

# output = "YES"