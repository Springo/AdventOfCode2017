def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d16input.txt")
strlines = []
for line in lines:
    splitline = line.split(',')
    strlines.append(splitline)

moves = strlines[0]

members = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
iters = 0
for _ in range(1000000000 % 48):
    iters += 1
    for m in moves:
        if m[0] == 's':
            shift = int(m[1:])
            m2 = members[-shift:]
            m2.extend(members[0:-shift])
            members = m2
        elif m[0] == 'x':
            nums = m[1:].split('/')
            a = int(nums[0])
            b = int(nums[1])
            temp = members[a]
            members[a] = members[b]
            members[b] = temp
        elif m[0] == 'p':
            lets = m[1:].split('/')
            a = members.index(lets[0])
            b = members.index(lets[1])
            temp = members[a]
            members[a] = members[b]
            members[b] = temp
        else:
            print("NO")

print(''.join(members))
print(iters)