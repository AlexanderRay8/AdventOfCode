def read_input():
    data = []
    with open('./2022/day4/day4_input.txt', 'r') as f:
        data = [ x.strip() for x in f.readlines()]
    return data

data = read_input()

# data =[ '2-4,6-8',
#         '2-3,4-5',
#         '5-7,7-9',
#         '2-8,3-7',
#         '6-6,4-6',
#         '2-6,4-8']

for i in range(len(data)):
    ranges = data[i].split(',')
    for j in range(len(ranges)):
        ranges[j] = tuple([int(x) for x in ranges[j].split('-')])
    data[i] = ranges

ctr = 0
for pair in data:
    low_a, high_a = pair[0]
    low_b, high_b = pair[1]
    if (low_a >= low_b
    and high_a <= high_b):
        ctr += 1
    
    elif (low_a <= low_b
    and high_a >= high_b):
        ctr += 1

print(ctr)

ctr = 0
for pair in data:
    low_a, high_a = pair[0]
    low_b, high_b = pair[1]
    if (low_a >= low_b
    and high_a <= high_b):
        ctr += 1
    
    elif (low_a <= low_b
    and high_a >= high_b):
        ctr += 1
    
    elif (high_a >= low_b and high_a <= high_b
    or low_a <= high_b and low_a >= low_b):
        ctr += 1
print(ctr)