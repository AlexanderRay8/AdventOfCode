
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2021/day3/input.txt', 'r') as f:
        input_lines = f.readlines()
        for i in range(len(input_lines)):
            input_lines[i] = input_lines[i].strip()
    return input_lines

def count_bits_at_pos(bitpos:int, numlist: list):
    zero_amt = 0
    one_amt = 0

    for num in numlist:
        if num[bitpos] == '0':
            zero_amt += 1
        if num[bitpos] == '1':
            one_amt += 1
    
    return (zero_amt, one_amt)

def find_most_candidates(bitpos:int, numlist: list):
    zero_amt, one_amt = count_bits_at_pos(bitpos, numlist)
    new_list = []
    bit = '1'
    if zero_amt > one_amt:
        bit = '0'
    
    for num in numlist:
        if num[bitpos] == bit:
            new_list.append(num)
    
    return new_list
    
def find_least_candidates(bitpos:int, numlist: list):
    zero_amt, one_amt = count_bits_at_pos(bitpos, numlist)
    new_list = []
    bit = '0'
    if one_amt < zero_amt:
        bit = '1'
    
    for num in numlist:
        if num[bitpos] == bit:
            new_list.append(num)
    
    return new_list


if __name__ == "__main__":

    input = read_input()

    zero_amt = [0] * len(input[0])
    one_amt = [0] * len(input[0])

    for num in input:
        for i in range(len(num)):
            if num[i] == '0':
                zero_amt[i] += 1
            if num[i] == '1':
                one_amt[i] += 1
    

    print(zero_amt)
    print(one_amt)
    
    cha_gamma = ''
    cha_epsilon = ''
    for i in range(len(zero_amt)):
        if zero_amt[i] > one_amt[i]:
            cha_gamma += '0'
            cha_epsilon += '1'
        else:
            cha_gamma += '1'
            cha_epsilon += '0'
    
    gamma = int(cha_gamma, base=2)
    epsilon = int(cha_epsilon, base=2)

    print(gamma)
    print(epsilon)
    print(gamma * epsilon)
    # 4139586
    
    oxygen = 0

    candidates = find_most_candidates(0, input)
    for i in range(1, len(cha_gamma)):
        candidates = find_most_candidates(i, candidates)
        if len(candidates) == 1:
            oxygen = int(candidates[0], base=2)
            break
        elif len(candidates) == 0:
            print("Error")

    carbon = 0
    candidates = find_least_candidates(0, input)
    for i in range(1, len(cha_gamma)):
        candidates = find_least_candidates(i, candidates)
        if len(candidates) == 1:
            carbon = int(candidates[0], base=2)
            break
        elif len(candidates) == 0:
            print("Error")


    print(carbon)
    print(oxygen * carbon)
    # 1800151