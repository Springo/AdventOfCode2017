def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d09input.txt")
line = lines[0]
i = 0
step = 0
score = 0
cancel = False
garbage = False
garbc = 0
while i < len(line):
    c = line[i]
    if c == '!':
        i += 1
    else:
        if garbage:
            garbc += 1
    if c == '<' and not garbage:
        garbage = True
    if c == '>' and garbage:
        garbage = False
        garbc -= 1
    if c == '{' and not garbage:
        step += 1
    if c == '}' and not garbage:
        score += step
        step -= 1
    i += 1
print(score)
print(garbc)