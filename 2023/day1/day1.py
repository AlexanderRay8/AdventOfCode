# imports
import re


# Sample Input
sample_input = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

sample_input2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

# New digits (part 2)
word_digits = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9}

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2023/day1/day_1input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input2.splitlines(keepends=True)]
    return input_lines

def find_first_and_last_digit(input_line:str) -> int:
    word_digit_pattern = f'\d|{"|".join(word_digits.keys())}'

    re_match = re.match(f'.*?({word_digit_pattern}).*({word_digit_pattern})', input_line)
    if re_match is not None:
         num = ''
         for digit in re_match.groups():
              if digit in word_digits.keys():
                   num += str(word_digits[digit])
              else:
                   num += digit
         return int(num)
    else:
         num = re.match(f'.*({word_digit_pattern}).*', input_line).group(1)
         if num in word_digits.keys():
              num = word_digits[num]
         return int(str(num) * 2)

if __name__ == "__main__":
    input_lines = read_input(True)
    total = 0
    for input_line in input_lines:
        print(input_line)
        print(find_first_and_last_digit(input_line))
        total += find_first_and_last_digit(input_line)
    print(total)