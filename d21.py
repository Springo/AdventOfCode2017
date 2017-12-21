def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d21input.txt")
#lines = readFile("test.txt")
strlines = dict()
for line in lines:
    splitline = line.split(' => ')
    s1 = splitline[0].split('/')
    s2 = splitline[1].split('/')
    s1mod = [list(a) for a in s1]
    s2mod = [list(a) for a in s2]
    strlines[str(s1mod)] = s2mod

image = [['.','#','.'],['.','.','#'],['#','#','#']]

def rotate(pat):
    return [list(a) for a in zip(*pat[::-1])]

def flip(pat):
    return pat[::-1]

for iter in range(18):
    newimage = []
    if len(image) % 2 == 0:
        for y in range(0, len(image), 2):
            for x in range(0, len(image[y]), 2):
                cell = [[image[y][x], image[y][x + 1]], [image[y + 1][x], image[y + 1][x + 1]]]
                cellr1 = rotate(cell)
                cellr2 = rotate(cellr1)
                cellr3 = rotate(cellr2)
                cellf1 = flip(cell)
                cellf2 = rotate(cellf1)
                cellf3 = rotate(cellf2)
                cellf4 = rotate(cellf3)
                cell = str(cell)
                cellr1 = str(cellr1)
                cellr2 = str(cellr2)
                cellr3 = str(cellr3)
                cellf1 = str(cellf1)
                cellf2 = str(cellf2)
                cellf3 = str(cellf3)
                cellf4 = str(cellf4)
                if cell in strlines:
                    newcell = strlines[cell]
                elif cellr1 in strlines:
                    newcell = strlines[cellr1]
                elif cellr2 in strlines:
                    newcell = strlines[cellr2]
                elif cellr3 in strlines:
                    newcell = strlines[cellr3]
                elif cellf1 in strlines:
                    newcell = strlines[cellf1]
                elif cellf2 in strlines:
                    newcell = strlines[cellf2]
                elif cellf3 in strlines:
                    newcell = strlines[cellf3]
                elif cellf4 in strlines:
                    newcell = strlines[cellf4]
                else:
                    print("NOOOO1")
                a = y // 2
                if a >= (len(newimage) // 3):
                    newimage.append([])
                    newimage.append([])
                    newimage.append([])
                newimage[a * 3].extend(newcell[0])
                newimage[a * 3 + 1].extend(newcell[1])
                newimage[a * 3 + 2].extend(newcell[2])
    elif len(image) % 3 == 0:
        for y in range(0, len(image), 3):
            for x in range(0, len(image[y]), 3):
                cell = [[image[y][x], image[y][x + 1], image[y][x + 2]],
                        [image[y + 1][x], image[y + 1][x + 1], image[y + 1][x + 2]],
                        [image[y + 2][x], image[y + 2][x + 1], image[y + 2][x + 2]]]
                cellr1 = rotate(cell)
                cellr2 = rotate(cellr1)
                cellr3 = rotate(cellr2)
                cellf1 = flip(cell)
                cellf2 = rotate(cellf1)
                cellf3 = rotate(cellf2)
                cellf4 = rotate(cellf3)
                cell = str(cell)
                cellr1 = str(cellr1)
                cellr2 = str(cellr2)
                cellr3 = str(cellr3)
                cellf1 = str(cellf1)
                cellf2 = str(cellf2)
                cellf3 = str(cellf3)
                cellf4 = str(cellf4)
                if cell in strlines:
                    newcell = strlines[cell]
                elif cellr1 in strlines:
                    newcell = strlines[cellr1]
                elif cellr2 in strlines:
                    newcell = strlines[cellr2]
                elif cellr3 in strlines:
                    newcell = strlines[cellr3]
                elif cellf1 in strlines:
                    newcell = strlines[cellf1]
                elif cellf2 in strlines:
                    newcell = strlines[cellf2]
                elif cellf3 in strlines:
                    newcell = strlines[cellf3]
                elif cellf4 in strlines:
                    newcell = strlines[cellf4]
                else:
                    print("NOOOO2")
                a = y // 3
                if a >= (len(newimage) // 4):
                    newimage.append([])
                    newimage.append([])
                    newimage.append([])
                    newimage.append([])
                newimage[a * 4].extend(newcell[0])
                newimage[a * 4 + 1].extend(newcell[1])
                newimage[a * 4 + 2].extend(newcell[2])
                newimage[a * 4 + 3].extend(newcell[3])
    else:
        print("WHAAAAT?")
    image = newimage
    print(len(image))
#    print(image)

counter = 0

for row in image:
#    print(row)
    for col in row:
        if col == '#':
            counter += 1
print(counter)

