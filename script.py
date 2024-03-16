def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[0][0] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'
    draw_board(board)
    for _ in range(9):
        row, col = map(int, input(f"Игрок {turn}, введите строку и столбец (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = turn
            draw_board(board)
            winner = check_winner(board)
            if winner:
                print(f"Игрок {winner} выйграл!")
                return
            turn = 'O' if turn == 'X' else 'X'
        else:
            print("Место занято!")
    print("It's a tie!")
tic_tac_toe()