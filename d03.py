grid = [[0] * 101 for _ in range(101)]
step = 1
grid[50][50] = 1
x = 51
y = 51
num = 265149


def sumgrid(grid, x, y):
    tot = grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1] + grid[x][y-1] + grid[x+1][y-1] + grid[x+1][y] + grid[x][y+1] + grid[x+1][y+1]
    return tot

while True:
    for i in range(2 * step - 1):
        y -= 1
        grid[x][y] = sumgrid(grid, x, y)
        if grid[x][y] > num:
            print(grid[x][y])
            exit()
    for i in range(2 * step - 1):
        x -= 1
        grid[x][y] = sumgrid(grid, x, y)
        if grid[x][y] > num:
            print(grid[x][y])
            exit()
    for i in range(2 * step - 1):
        y += 1
        grid[x][y] = sumgrid(grid, x, y)
        if grid[x][y] > num:
            print(grid[x][y])
            exit()
    for i in range(2 * step - 1):
        x += 1
        grid[x][y] = sumgrid(grid, x, y)
        if grid[x][y] > num:
            print(grid[x][y])
            exit()
    step += 1
    x += 1
    y += 1