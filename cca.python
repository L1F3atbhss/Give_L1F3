import random

# Create an empty 3x3 board
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_win(player):
    # Rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # row
            return True
        if all([board[j][i] == player for j in range(3)]):  # column
            return True
    if all([board[i][i] == player for i in range(3)]):  # main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # anti-diagonal
        return True
    return False

def is_draw():
    return all([cell != " " for row in board for cell in row])

def player_move():
    while True:
        try:
            move = input("Enter your move (row and column: 0 1): ")
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already taken!")
        except:
            print("Invalid input. Enter two numbers (0, 1 or 2) separated by a space.")

def computer_move():
    print("Computer's move:")
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

# Main Game Loop
print("Tic-Tac-Toe! You are X, computer is O.")
print_board()

while True:
    player_move()
    print_board()
    if check_win("X"):
        print("You win!")
        break
    if is_draw():
        print("It's a draw!")
        break

    computer_move()
    print_board()
    if check_win("O"):
        print("Computer wins!")
        break
    if is_draw():
        print("It's a draw!")
        break
