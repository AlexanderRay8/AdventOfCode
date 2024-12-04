# imports
import re


# Sample Input
sample_input = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2024/day3/day_3input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines



if __name__ == "__main__":
    input_lines = read_input(True)
    mul_pattern = r"(do(?!n't))|(don't)|mul\((\d{1,3}),(\d{1,3})\)"
    dot_product = 0
    do = True
    mul_list = []
    for line in input_lines:
        for mul_match in re.findall(mul_pattern, line):
            if mul_match[0]:
                do = True
            elif mul_match[1]:
                do = False
            else:
                if do == True:
                    mul_list.append((mul_match[2], mul_match[3]))
    for mul in mul_list:
        dot_product += int(mul[0]) * int(mul[1])
    print(dot_product)