
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2022/day8/day_8input.txt', 'r') as f:
        input_lines = [x.strip() for x in f.readlines()]
    return input_lines

def sample_input():
    return """\
30373
25512
65332
33549
35390""".splitlines()

if __name__ == "__main__":
    input_lines = sample_input()
    tree_grid = []
    for line in input_lines:
        tree_line = []
        for height in line:
            tree_line.append(int(height))
        tree_grid.append(tree_line)

    visible_count = 0
    for xIndex, grid in enumerate(tree_grid):
        for yIndex, height in enumerate(grid):
            if ((xIndex == 0) or (yIndex == 0) or
                (xIndex == len(grid) - 1) or
                (yIndex == len(grid) - 1)):
                visible_count += 1

        print()
    print(tree_grid)