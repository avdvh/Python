# Initialize the board
board = [" " for _ in range(9)]

# Function to display the Tic Tac Toe board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_win(player):
    # Check rows, columns, and diagonals
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Main game loop
def play_game():
    current_player = "X"
    while True:
        display_board()
        print(f"Player {current_player}'s turn. Enter a position (1-9): ")
        try:
            position = int(input()) - 1
            if position < 0 or position > 8 or board[position] != " ":
                print("Invalid move. Try again.")
                continue
            board[position] = current_player
            if check_win(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break
            if " " not in board:
                display_board()
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

# Start the game
if __name__ == "__main__":
    play_game()
