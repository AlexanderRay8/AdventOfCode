# imports



# Sample Input
sample_input = """\
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2024/day1/day_1input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines



if __name__ == "__main__":
    input_lines = read_input(True)

    
    left_list = []
    right_list = []

    for line in input_lines:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))
    
    left_list.sort()
    right_list.sort()

    # subtract + abs value
    diffs = []
    for i in range(len(left_list)):
        diffs.append(abs(left_list[i] - right_list[i]))
    
    # add differences
    print(sum(diffs))

    # Part 2
    # dict of left list nums with count of right list
    # multiply num by count for all of left list
    # sum products
    # ???
    # profit

    # dict
    left_counts = dict.fromkeys(set(left_list), 0)
    for num in right_list:
        if num in left_counts.keys():
            left_counts[num] += 1
    
    # multiply
    left_product = []
    for num in left_list:
        left_product.append(num * left_counts[num])
    
    # sum prodcuts
    print(sum(left_product))