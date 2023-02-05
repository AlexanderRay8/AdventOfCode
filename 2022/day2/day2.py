
def read_input():
    data = []
    with open('./2022/day2/day2_input.txt', 'r') as f:
        data = [lambda: x.strip() for x in f.readlines()]
    return data

data = read_input()