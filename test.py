grid = [[None] * 4 for i in range(4)]
print(grid, "\n")
for i, c in enumerate(grid):
    print(grid[i])
    for j, c2 in enumerate(grid[i]):
        print(grid[i][j])
        grid[i][j] = list()

print("\n", grid, sep='')
grid[0][3].append(5)
grid[0][3].append(7)
print("\n", grid, sep='')
