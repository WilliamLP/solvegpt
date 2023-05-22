def is_valid(board, row, col, num):
    # Check the number in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check the number in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check the number in the box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True

def solve_and_sum(file_name):
    sum_ = 0
    with open(file_name, 'r') as f:
        while True:
            puzzle = []
            try:
                for _ in range(9):
                    line = next(f)
                    puzzle.append(list(map(int, list(line.strip()))))
                solve_sudoku(puzzle)
                sum_ += int(''.join(map(str, puzzle[0][:3])))
                print(sum_)
            except ValueError:
                continue
            except StopIteration:
                break
    return sum_

print(solve_and_sum('sudoku.txt'))
