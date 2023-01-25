
def read_input():
    data = []
    with open('./2022/day3/day3_input.txt', 'r') as f:
        data = [ x.strip() for x in f.readlines()]
    return data

data = read_input()
# data = [
#     'vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]

sum = 0
for i in range(0, len(data), 3):

    first_set = set(data[i])
    second_set = set(data[i+1])
    third_set = set(data[i+2])
    
    c = first_set.intersection(second_set).intersection(third_set).pop()
    if c.islower():
        sum += ord(c) - ord('a') + 1
    else:
        sum += ord(c) - ord('A') + 27

print(sum)