def read_input():
    data = []
    with open('./2021/day5_input.txt', 'r') as f:
        data = [tuple([tuple([int(n) for n in c.split(',')]) for c in x.strip().split(' -> ')]) for x in f.readlines()]
    return data

def print_map(vent_map: list):
    for row in vent_map:
        row_str = ''
        for num in row:
            if num == 0:
                row_str += '.'
            else:
                row_str += str(num)
        print(row_str)


input_lines = read_input()
print(input_lines[0])
vent_map = [[0 for _ in range(1000)] for _ in range(1000)]
input_lines = [input_lines[0]]
for line in input_lines:
    for start, end in line:
        x_diff = abs(end[0] - start[0])
        y_diff = abs(end[1] - start[1])

        for dx in range(x_diff + 1):
            vent_map[start[0] + dx][start[1]] += 1
        
        for dy in range(y_diff + 1):
            vent_map[start[0]][start[1] + dx] += 1
        
        print_map(vent_map)
