grid = [[8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3]]
highcol = []
for c in range(len(grid)):
    highc = 0
    for r in range(len(grid)):
        if grid[r][c] > highc:
            highc = grid[r][c]
    highcol.append(highc)

print(highcol)
print([z for z in zip(*grid)])
