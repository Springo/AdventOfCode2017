def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d22input.txt")
grid = []

pad = 1000

for pre in range(pad):
    grid.append(['.'] * (2 * pad + len(lines[0])))

for line in lines:
    newline = ['.'] * pad
    newline.extend(line)
    newline.extend(['.'] * pad)
    grid.append(newline)

for post in range(pad):
    grid.append(['.'] * (2 * pad + len(lines[0])))

print(len(grid))
print(len(grid[0]))

x = len(grid) // 2
y = len(grid[x]) // 2
dir = 0
inf = 0

for b in range(10000000):
    if grid[y][x] == '#':
        dir = (dir + 1) % 4
        grid[y][x] = 'F'
    elif grid[y][x] == '.':
        dir = (dir - 1) % 4
        grid[y][x] = 'W'
    elif grid[y][x] == 'F':
        dir = (dir + 2) % 4
        grid[y][x] = '.'
    elif grid[y][x] == 'W':
        grid[y][x] = '#'
        inf += 1
    else:
        print("NO")
    if dir == 0:
        y -= 1
    elif dir == 2:
        y += 1
    elif dir == 1:
        x += 1
    elif dir == 3:
        x -= 1
print(inf)