def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True


def print_solution(board, n):
    for row in board:
        for cell in row:
            print('Q' if cell else '.', end=' ')
        print()
    print()


def solve(row, n, board, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(row + 1, n, board, solutions)
            board[row][col] = 0


def main():
    n = int(input("Enter N: "))
    
    if n < 1:
        print("Invalid size")
        return
    
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    solve(0, n, board, solutions)
    
    print(f"\nFound {len(solutions)} solutions for N={n}\n")
    
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print_solution(sol, n)


if __name__ == "__main__":
    main()