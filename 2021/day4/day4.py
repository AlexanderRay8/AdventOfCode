
def read_input():
    input_lines = []
    with open('/home/alex/coding/AdventOfCode/2021/day4/day_4input.txt', 'r') as f:
        input_lines = [x.strip() for x in f.readlines()]
    return input_lines

def check_win(board: list, win_set: set):
    # Boards are all 5x5
    # Check all rows
    for row in board:
        no_win = False
        for num in row:
            if num not in win_set:
                no_win = True
                break
        if no_win == False:
            return True
    
    # Check all columns
    for a in range(len(board)):
        no_win = False
        for b in range(len(board[a])):
            if board[b][a] not in win_set:
                no_win = True
                break
        if no_win == False:
            return True
    return False

def calculate_score(board, win_set, winning_num):
    score = 0
    for row in board:
        for num in row:
            if num not in win_set:
                score += num
    return score * winning_num

if __name__ == "__main__":
    input_lines = read_input()
    
    winning_nums = [int(n) for n in input_lines[0].split(',')]

    boards = [[[int(n) for n in board.split()] for board in input_lines[i:i+5]] for i in range(2, len(input_lines), 6)]

    win_set = set()
    found_win = False
    board_win = set(range(len(boards)))

    for win_num in winning_nums:
        win_set.add(win_num)
        for i in range(len(boards)):
            if check_win(boards[i], win_set):
                if len(board_win) == 1 and i in board_win:
                    print(calculate_score(boards[board_win.pop()], win_set, win_num))
                    found_win = True
                    break
                board_win.discard(i)
        if found_win == True:
            break

