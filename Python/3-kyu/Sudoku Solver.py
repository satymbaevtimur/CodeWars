def is_valid(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def sudoku(puzzle):
    empty_location = find_empty_location(puzzle)

    if not empty_location:
        return puzzle

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num

            if sudoku(puzzle):
                return puzzle

            puzzle[row][col] = 0

    return None
