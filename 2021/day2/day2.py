
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2021/day2/input.txt', 'r') as f:
        input_lines = f.readlines()
        for i in range(len(input_lines)):
            input_lines[i] = input_lines[i].strip().split()
            input_lines[i][1] = int(input_lines[i][1])
    return input_lines

if __name__ == "__main__":
    input = read_input()

    DIRECTION = 0
    AMOUNT = 1

    pos = 0
    depth = 0

    for move in input:
        if move[DIRECTION] == 'forward':
            pos += move[AMOUNT]
        if move[DIRECTION] == 'down':
            depth += move[AMOUNT]
        if move[DIRECTION] == 'up':
            depth -= move[AMOUNT]

    print(pos * depth)
    # 2070300

    aim = 0
    pos = 0
    depth = 0

    for move in input:
        if move[DIRECTION] == 'forward':
            pos += move[AMOUNT]
            depth += move[AMOUNT] * aim
        if move[DIRECTION] == 'down':
            aim += move[AMOUNT]
        if move[DIRECTION] == 'up':
            aim -= move[AMOUNT]
    
    print(pos * depth)
    # 2078985210