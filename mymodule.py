board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
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





