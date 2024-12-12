# imports



# Sample Input
sample_input = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2024/day6/day_6input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines

def find_guard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in ['v', '<', '^','>']:
                return ([i, j], map[i][j])

def count_positions(map):
    pos_count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'X':
                pos_count += 1
    return pos_count

class Guard:
    def __init__(self, map):
        self.pos, self.dir = find_guard(map)
        self.map = map
        self.find_next_pos()

    def turn_guard(self):
        dir_list = ['v', '<', '^', '>']
        dir_idx = dir_list.index(self.dir) + 1
        if dir_idx == len(dir_list):
            dir_idx = 0
        self.map[self.pos[0]][self.pos[1]] = dir_list[dir_idx]
        self.dir = dir_list[dir_idx]

    def advance_guard(self):
        self.map[self.next_pos[0]][self.next_pos[1]] = self.dir
        self.map[self.pos[0]][self.pos[1]] = 'X'
        self.pos = self.next_pos

    def find_next_pos(self):
        match (self.dir):
            case 'v':
                if self.pos[0]+1 == len(self.map):
                    self.next_pos = None
                else:
                    self.next_pos =  [self.pos[0]+1, self.pos[1]]
            case '<':
                if self.pos[1]-1 == -1:
                    self.next_pos = None
                else:
                    self.next_pos = [self.pos[0], self.pos[1]-1]
            case '^':
                if self.pos[0]-1 == -1:
                    self.next_pos = None
                else:
                    self.next_pos = [self.pos[0]-1, self.pos[1]]
            case '>':
                if self.pos[1]+1 == len(self.map):
                    self.next_pos = None
                else:
                    self.next_pos = [self.pos[0], self.pos[1]+1]
            case _:
                self.next_pos = None

    def move_guard(self):
        self.find_next_pos()
        if self.next_pos is None:
            self.map[self.pos[0]][self.pos[1]] = 'X'
            self.pos = None
        elif self.map[self.next_pos[0]][self.next_pos[1]] == '#':
            self.turn_guard()
            self.find_next_pos()
        elif self.map[self.next_pos[0]][self.next_pos[1]] == 'X' or self.map[self.next_pos[0]][self.next_pos[1]] == '.':
            self.advance_guard()

if __name__ == "__main__":
    input_lines = read_input(True)
    map = [list(line) for line in input_lines]
    guard = Guard(map)

    while guard.pos is not None:
        guard.move_guard()
    print(count_positions(map))