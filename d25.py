checksum = 12261543

state = 'A'
tape = [0]
point = 0

def move(amount):
    global tape
    global point
    if amount == 1:
        point += 1
        if point >= len(tape):
            tape.append(0)
    elif amount == -1:
        point -= 1
        if point < 0:
            point += 1
            tape.insert(0, 0)


for i in range(checksum):
    val = tape[point]
    if state == 'A':
        if val == 0:
            tape[point] = 1
            move(1)
            state = 'B'
        else:
            tape[point] = 0
            move(-1)
            state = 'C'
    elif state == 'B':
        if val == 0:
            tape[point] = 1
            move(-1)
            state = 'A'
        else:
            move(1)
            state = 'C'
    elif state == 'C':
        if val == 0:
            tape[point] = 1
            move(1)
            state = 'A'
        else:
            tape[point] = 0
            move(-1)
            state = 'D'
    elif state == 'D':
        if val == 0:
            tape[point] = 1
            move(-1)
            state = 'E'
        else:
            move(-1)
            state = 'C'
    elif state == 'E':
        if val == 0:
            tape[point] = 1
            move(1)
            state = 'F'
        else:
            move(1)
            state = 'A'
    elif state == 'F':
        if val == 0:
            tape[point] = 1
            move(1)
            state = 'A'
        else:
            move(1)
            state = 'E'
print(tape.count(1))
