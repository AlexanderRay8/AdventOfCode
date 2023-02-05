
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2022/day5/day_5input.txt', 'r') as f:
        input_lines = [x for x in f.readlines()]
    return input_lines

def sample_input():
    return """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines(keepends=True)

def create_stacks(crate_positions: list):
    num_stacks = len(crate_positions.pop().split())
    crates = [list() for _ in range(num_stacks)]
    for line in reversed(crate_positions):
        # Split crates into sections to add
        for i in range(0, len(line), 4):
            if line[i+1].isalpha():
                crates[i >> 2].append(line[i+1])
    return crates

def find_tallest_stack(crates:list):
    return max([len(stack) for stack in crates])

def print_stacks(crates:list):
    num_stacks = len(crates)
    height = find_tallest_stack(crates)
    diagram = ''
    for i in range(height - 1, -1, -1):
        row = ''
        for stack in crates:
            if len(stack) > i:
                row += f'[{stack[i]}] '
            else: # Empty slot
                row += '    '
        diagram += f'{row[:-1]}\n'
    diagram += ' '.join([f' {num} ' for num in range(1, num_stacks+1)])
    print(diagram)

def parse_instruction(instruction: str):
    inst_list = []
    for x in instruction.split():
        if x.isdigit():
            inst_list.append(int(x))
    # Will return (Quantity, Source, Destination)
    return inst_list


def execute_instructions(instructions:list, crates:list, is_9001:bool=False):
    for instruction in instructions:
        quantity, src, dest = parse_instruction(instruction)
        transfers = []
        for _ in range(quantity):
            transfers.append(crates[src-1].pop())
        if is_9001:
            transfers.reverse()
        crates[dest-1] += transfers


def print_results(crates:list):
    print(''.join([stack[-1] if len(stack) else '' for stack in crates]))

if __name__ == "__main__":
    input_lines = sample_input()

    crate_positions = []
    move_instructions = []
    is_diagram = True
    for line in input_lines:
        if line == '\n':
            is_diagram = False
            continue
        if is_diagram:
            crate_positions.append(line)
        else:
            move_instructions.append(line)

    crates = create_stacks(crate_positions)
    print_stacks(crates)
    execute_instructions(move_instructions, crates, True)
    print_stacks(crates)
    print_results(crates)