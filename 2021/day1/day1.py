
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2021/day1/input.txt', 'r') as f:
        input_lines = f.readlines()
    for i in range(len(input_lines)):
        input_lines[i] = int(input_lines[i].strip())
    return input_lines

if __name__ == "__main__":
    input = read_input()

    inc_count = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            inc_count += 1

    print(inc_count)
    # 1688
    
    inc_count = 0
    prev_window_val = input[0] + input[1] + input[2]
    for i in range(3, len(input)):
        cur_window_val = prev_window_val + input[i] - input[i - 3]
        if cur_window_val > prev_window_val:
            inc_count += 1
        prev_window_val = cur_window_val

    print(inc_count)
    # 1728