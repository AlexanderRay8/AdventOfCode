# imports



# Sample Input
sample_input = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2025/day1/day_1input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines

def rotate_right(dial, rot_amount, zero_count):
    new_dial = dial + rot_amount % 100
    zero_count += rot_amount // 100
    if new_dial >= 100:
        return (new_dial - 100, zero_count + (not dial == 0))
    else:
        return (new_dial, zero_count)

def rotate_left(dial, rot_amount, zero_count):
    new_dial = dial - rot_amount % 100
    zero_count += rot_amount // 100
    if new_dial < 0:
        return (new_dial + 100, zero_count + (not dial == 0)) 
    elif new_dial == 0:
        return (new_dial, zero_count + 1)
    else:
        return (new_dial, zero_count) 

def process_input(input_line:str):
    if len(input_line) == 0:
        return (None, None)
    direction = input_line[0]
    rot_amount = int(input_line[1:])

    return (direction, rot_amount)


if __name__ == "__main__":
    input_lines = read_input(True)
    dial = 50
    count = 0

    for line in input_lines:
        direction, rot_amount = process_input(line)

        if direction == 'L':
            dial, count = rotate_left(dial, rot_amount, count)
        elif direction == 'R':
            dial, count = rotate_right(dial, rot_amount, count)
        else:
            continue

    print(count)
