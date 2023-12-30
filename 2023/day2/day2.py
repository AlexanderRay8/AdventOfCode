# imports
import re

# Sample Input
sample_input = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()
    
def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2023/day2/day_2input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines



def validate_round(round_dict:dict):
    max_cube_dict = {'red': 12,
                     'green': 13,
                     'blue': 14}
    for color in max_cube_dict.keys():
        if round_dict[color] > max_cube_dict[color]:
            return False
    return True

def parse_input(input: str):
    input_pattern = r'(?: ?\d+ \w+,?)+'
    game_rounds = re.findall(input_pattern, input)
    
    valid_game = True
    for round in game_rounds:
        round_dict = dict(red=0, green=0, blue=0)
        colors = [x.strip() for x in round.split(',')]
        for desc in colors:
            number, color = desc.split(' ')
            round_dict[color] = int(number)
        
        if not validate_round(round_dict):
            valid_game = False     

    return valid_game






if __name__ == "__main__":
    input_lines = read_input(True)
    id_sum = 0
    id = 1
    for line in input_lines:
        id_sum += id * parse_input(line)
        id += 1
    print(id_sum)
