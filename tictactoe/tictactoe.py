board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

cross = 'X'
nought = 'O'
nothing = '_'
max_turns = 9
counter = 0 

playerpos = {cross: [], nought: []}


def player_goes(counter):
    if (counter + 2) % 2 == 0:
        print('Крестик ходит)')
        changed_board(cross)
    else:
        print('Нолик ходит)')
        changed_board(nought)


def changed_board(sym):
    global board
    print()
    line_coordinate = int(input())
    column_coordinate = int(input())
    if board[line_coordinate - 1][column_coordinate - 1] != nothing:
        print('Данная клетка уже занята! Введите другие координаты')
        return changed_board(sym)
    else: 
        board[line_coordinate - 1][column_coordinate - 1] = sym
        print()
        print(' '.join(board[0]))
        print(' '.join(board[1]))
        print(' '.join(board[2]))
        print()

#assert(changed_board(nought) 
#     line_coordinate = 1 
#    column_coordinate = 1 
#   board = [[cross, nothing, nothing],
#             [nothing, nothing, nothing],
#              [nothing, nothing, nothing]])


def who_wins(board):
    win_coords = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for win in win_coords:
        if win[0] == win[1] == win[2]:
            return win[0]
    return nothing


def who_wins_check(board):
    global counter
    winner = who_wins(board)
    if winner == nought:
        print('Игра окончена! Нолики победили!')
        quit() 
    elif winner == cross:
        print('Игра окончена! Крестики победили!')
        quit()
    else:
        counter += 1 
        if counter == 9:
            print('Ничья!')
            quit()


def game():
    player_goes(counter)
    who_wins(board)
    who_wins_check(board)


import Tictactoe.mymodule as mymodule
mymodule.game_rules()
for i in range(max_turns):
        game()
