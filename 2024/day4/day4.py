# imports

# Sample Input
sample_input = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()

def read_input(use_real_input=False):
    input_lines = []
    if use_real_input:
        with open('/home/alex/AdventOfCode/2024/day4/day_4input.txt', 'r') as f:
            input_lines = [x.strip() for x in f.readlines()]
    else:
            input_lines = [x.strip() for x in sample_input.splitlines(keepends=True)]
    return input_lines

def follow_word(word_search, row, col, r, c):
    direction = (r - row, c - col)
    # Check bounds
    if r - row < 0 and r - 2 < 0:
        return False
    if r - row > 0 and r + 2 > len(word_search[r]) -1:
        return False
    if c - col < 0 and c - 2 < 0:
        return False
    if c - col > 0 and c + 2 > len(word_search[c]) -1:
        return False
    # Check word
    if (word_search[r + direction[0]][c + direction[1]] == 'A' and 
        word_search[r + 2 * direction[0]][c + 2 * direction[1]] == 'S'):
        return True
    return False


def search_perimeter(xmas_cnt, word_search, row, col):
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            # Check if outside word grid
            if (r == -1 or r >= len(word_search) or 
                (c == -1 or c >= len(word_search[r])) or
                (r == 0 and c == 0)):
                continue
            # Check 2nd letter
            if word_search[r][c] == 'M':
                xmas_cnt += follow_word(word_search, row, col, r, c)
    return xmas_cnt


if __name__ == "__main__":
    input_lines = read_input()

    xmas_cnt = 0
    for r in range(len(input_lines)):
        for c in range(len(input_lines[r])):
            if input_lines[r][c] == 'X':
                xmas_cnt = search_perimeter(xmas_cnt, input_lines, r, c)

    print(xmas_cnt)