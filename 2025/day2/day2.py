# imports



# Sample Input
sample_input = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2025/day2/day_2input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines

def process_input(input_lines: list[str]):
    ranges = []
    for line in input_lines:
        ranges.extend([l for l in line.split(',') if l != ''])
    return ranges

if __name__ == "__main__":
    input_lines = read_input()
    ranges = process_input(input_lines)

    print(ranges)