
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2022/day6/day_6input.txt', 'r') as f:
        input_lines = [x.strip() for x in f.readlines()][0]
    return input_lines

sample_input = 'bvwbjplbgvbhsrlpgdmjqwftvncz' # answer is 5
sample_input2 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' # answer is 7

def process_signal(input_signal: str) -> int:
    for i in range(len(input_signal) - 14):
        buffer_set = set(input_signal[i:i+14])
        if len(buffer_set) == 14:
            return i+14

if __name__ == "__main__":
    input_lines = read_input()

    # input_lines = sample_input2 # Comment out to test with real input

    signal_marker = process_signal(input_lines)
    print(signal_marker)
