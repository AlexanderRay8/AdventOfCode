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

def validate_id(id: int):
    str_id = str(id)
    pattern = []
    idx = 0

    for idx, digit in enumerate(str_id):
        if idx + len(pattern) > len(str_id):
            return False
        if str_id[idx:idx + len(pattern)] == "".join(pattern) and len(pattern) > 0:
            if "".join(pattern) * (len(str_id) // len(pattern)) == str_id and (len(str_id) // len(pattern) > 1):
                return True
        pattern.append(digit)
    return "".join(pattern) * (len(str_id) // len(pattern)) == str_id and (len(str_id) // len(pattern) > 1)
    

if __name__ == "__main__":
    input_lines = read_input(True)
    ranges = process_input(input_lines)
    id_sum = 0
    for id_range in ranges:
        start, end = [int(x) for x in id_range.split('-')]
        for id in range(start, end+1):
            is_valid = validate_id(id)
            if is_valid:
                id_sum += id

    print(id_sum)