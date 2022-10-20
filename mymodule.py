board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

def empty_board():
    print(' '.join(board[0]))
    print(' '.join(board[1]))
    print(' '.join(board[2]))

def game_rules():
    print('Привет! Это экспериментальная версия игры крестики-нолики!')
    print()
    print('Для продолжения нажимайте Enter')
    input()
    print('Для начала объясню принцип игры:')
    print('Чтобы сходить - нужно написать 2 числа.')
    print('Первое число - номер строки сверху, от 1 до 3.')
    print('А второе - номер столбика, идентично от 1 до 3 :)')
    print('Если вы хотите остановить игру - напишите stop')
    print('А если хотите продолжить игру - напишите countinue')
    input()
    print('Теперь выберите за кого вы будете играть)')
    input()
    print('А теперь давай играть!')
    empty_board()
    print()


cross = 'X'
nought = 'O'
nothing = '_'


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

    assert(who_wins([
    [cross, cross, cross],
    [nothing, nothing, nothing],
    [nothing, nothing, nothing]
]) == cross)

