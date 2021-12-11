import os
os.system("cls")

def mark_island(grid, i, j):
    ## if point is not valid quit!
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return

    ## Ensure you mark point as visited turn 1 to 0 
    
    grid[i][j] = 0
    
    # Explore neighbors depthwise 
    
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ## This is simply DFS of the Graph
    
    for d in dirs:
        mark_island(grid, i + d[0], j + d[1])

def num_islands(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                mark_island(grid, i, j)
                count += 1

    return count


grid1 = [
    [1,1,1,1,1],
    [0,0,0,0,1],
    [0,0,1,1,1],
    [1,1,1,0,0],
]

grid2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1],
]

print(num_islands(grid1))
print(num_islands(grid2))