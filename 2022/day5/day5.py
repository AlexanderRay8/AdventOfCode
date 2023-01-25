
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2022/day5/day_5input.txt', 'r') as f:
        input_lines = [x.strip() for x in f.readlines()]
    return input_lines

if __name__ == "__main__":
    input_lines = read_input()

    start_pos = []
    crates = [] # list of stacks. index is stack number - 1
    instructions = []
    is_inst = False
    for line in input_lines:
        if line == '': # reached end of starting position
            is_inst = True
            continue
        if is_inst:
            instructions.append(line)
        else: # starting diagram
            start_pos.append(line)


    start_pos.pop() # removes bottom numbers
    for row in start_pos.reverse():
        for crate in range(0, len(row), 3):
            if row[crate] == '[':
                crates[]

