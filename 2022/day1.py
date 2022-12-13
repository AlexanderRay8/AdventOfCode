data = []
with open('./2022/day1_input.txt', 'r') as f:
    cur = 0
    for line in f.readlines():
        line = line.strip()
        if line == '': # we have gotten all the calories
            data.append(cur)
            cur = 0
        else:
            cur += int(line)

data.sort()
max = data[-1]
top3 = sum(data[-3:])

print(max)
print(top3)

