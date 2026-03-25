import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\n")
    print(f"  {board[0]} | {board[1]} | {board[2]}  ")
    print(" ---|---|---")
    print(f"  {board[3]} | {board[4]} | {board[5]}  ")
    print(" ---|---|---")
    print(f"  {board[6]} | {board[7]} | {board[8]}  ")
    print()

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def get_move(board, player):
    while True:
        try:
            move = int(input(f"  Player {player}, enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                return move
            else:
                print("  Invalid move. Try again.")
        except ValueError:
            print("  Please enter a number 1-9.")

def play():
    while True:
        board = [str(i+1) for i in range(9)]
        current = 'X'

        print("\n=== TIC TAC TOE ===")
        print("Positions:")
        print_board(board)

        while True:
            print_board(board)
            move = get_move(board, current)
            board[move] = current

            if check_winner(board, current):
                print_board(board)
                print(f"  Player {current} wins!\n")
                break

            if is_draw(board):
                print_board(board)
                print("  It's a draw!\n")
                break

            current = 'O' if current == 'X' else 'X'

        again = input("  Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n  Thanks for playing!\n")
            break

if __name__ == "__main__":
    play()
