def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d11input.txt")
steps = lines[0].split(',')
print(steps)

highest = 0
y = 0
x = 0
for s in steps:
    if s[0] == 's':
        y -= 1
        if s[-1] == 'e':
            x += 1
        elif s[-1] == 'w':
            x -= 1
        else:
            y -= 1
    else:
        y += 1
        if s[-1] == 'e':
            x += 1
        elif s[-1] == 'w':
            x -= 1
        else:
            y += 1
    stps = max(abs(x), (abs(y) - abs(x)) // 2 + abs(x))
    if stps > highest:
        highest = stps

print(max(abs(x), (abs(y) - abs(x)) // 2 + abs(x)))
print(highest)