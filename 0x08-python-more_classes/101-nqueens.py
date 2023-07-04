#!/usr/bin/python3
import sys


def is_valid_move(board, row, col):
    """
    Check if a queen can be placed on board[row][col]

    Arguments:
    board -- the current state of the chessboard
    row -- the row to check
    col -- the column to check

    Returns:
    True if a queen can be placed at (row, col), False otherwise
    """

    # Check this row on the left side
    if 1 in board[row][:col]:
        return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, solutions):
    """
    Solve the N queens problem recursively.

    Args:
        board: The N x N chessboard represented as a 2D list.
        col: The current column being processed.
        solutions: A list to store the valid solutions.

    Returns:
        True if a solution is found, False otherwise.
    """
    N = len(board)

    # Base case: If all queens are placed, add the solution
    if col == N:
        # Extract the positions of the queens from the board
        solution = [[i + 1 for i in range(N) if board[j][i] == 1] for j in range(N)]
        solutions.append(solution)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for row in range(N):
        if is_valid_move(board, row, col):
            # Place a queen at (row, col)
            board[row][col] = 1

            # Recursively solve for the next column
            solve_n_queens(board, col + 1, solutions)

            # Backtrack by removing the queen from (row, col)
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print all valid solutions to the N queens problem.

    Args:
        solutions: A list of valid solutions.
    """
    for solution in solutions:
        print("\n".join(" ".join(str(col) for col in row) for row in solution))
        print()


if __name__ == "__main__":
    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Initialize an empty NxN chessboard
    board = [[0] * N for _ in range(N)]

    # Solve the N queens problem and print all valid solutions
    solutions = []
    solve_n_queens(board, 0, solutions)
    
    if not solutions:
        print(f"No solution found for {N}x{N} chessboard.")
    
    print_solutions(solutions)
