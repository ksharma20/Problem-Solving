# Problem - https://www.codingame.com/training/medium/there-is-no-spoon-episode-1
# Skills Needed: Python Lists, Multidimenstional Array.

grid = []
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = list(input())  # width characters, each either 0 or .
    grid.append(line)

print(grid, "\n ------------------------", file=sys.stderr, flush=True)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Three coordinates: a node, its right neighbor, its bottom neighbor

for row in range(height):
    for col in range(width):
        nb = ''
        if grid[row][col] == '0':
            nb += f'{col} {row}'
            for incol in range(col+1,width):
                if grid[row][incol] == '0':
                    nb += f' {incol} {row}'
                    break
            if len(nb) < 4:
                nb += ' -1 -1'
            for inrow in range(row+1,height):
                if grid[inrow][col] == '0':
                    nb += f' {col} {inrow}'
                    break
            if len(nb) < 10:
                nb += ' -1 -1'
        else: continue
        grid[row][col] = nb
        print(grid, file=sys.stderr, flush=True)
        print(nb)

