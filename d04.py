def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d04input.txt")
count = 0
for line in lines:
    words = dict()
    splitline = line.split()
    dup = False
    for word in splitline:
        if str(sorted(word)) in words:
            dup = True
        else:
            words[str(sorted(word))] = 1
    if not dup:
        count += 1
print(count)
