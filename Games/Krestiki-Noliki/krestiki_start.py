from base import *

instructions()
computer, human = pieces()
turn = X
board = new_board()
display_board(board)
while not winner(board):
    if turn == human:
        move = human_move(board, human)
        board[move] = human
    else:
        move = computer_move(board, computer, human)
        board[move] = computer
    display_board(board)
    turn = next_turn(turn)
the_winner = winner(board)
congrat_winner(the_winner, computer, human)
input('Нажмите Enter, чтобы выйти... ')
