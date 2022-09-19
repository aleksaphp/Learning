a = ['','_', '_', '_']
b = ['','_', '_', '_']
c = ['','_', '_', '_']

board = [
    [],
    [],
    []
]

def empty_board():
    global a, b, c
    print(' '.join(a))
    print(' '.join(b))
    print(' '.join(c))

def x_goes():
    print('Крестик ходит)')

def o_goes():
    print('Нолик ходит)')

def input_turn(sym):
    global a, b, c
    y = int(input())
    z = int(input())
    if y == 1:
        a[z] = sym
    elif y == 2:
        b[z] = sym
    elif y == 3:
        c[z] = sym
    print(' '.join(a))
    print(' '.join(b))
    print(' '.join(c))

def who_wins_check(board):
    if board[0][0] == 'o':
        return 'o'
    else:
        return 'x'

def who_wins(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return who_wins_check()
    else:
        return '_'
test_board = [
    ['o', 'o', 'o'],
    [],
    []
]
test_board1 = [
    ['o', '_', '_'],
    ['_', 'o', '_'],
    ['_', '_', 'o'],
]
assert(who_wins(test_board) == 'o')
assert(who_wins(test_board1) == 'o')

def game_over():
    global board
    winner = who_wins(board)
    if winner == 'x':
        print("Игра окончена! Крестики победили!")
    else:
        print("Игра окончена! Нолики победили!")
    quit()


def game_over():
    if a[1] == a[2] == a[3] and a[1] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif b[1] == b[2] == b[3] and b[1] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif c[1] == c[2] == c[3] and c[1] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif a[1] == b[1] == c[1] and a[1] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif a[2] == b[2] == c[2] and a[2] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif a[3] == b[3] == c[3] and a[3] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif a[1] == b[2] == c[3] and a[1] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif a[3] == b[2] == c[1] and a[3] == 'x':
        print("Игра окончена! Крестики победили!")
        quit()
    elif a[1] == a[2] == a[3] and a[1] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif b[1] == b[2] == b[3] and b[1] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif c[1] == c[2] == c[3] and c[1] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif a[1] == b[1] == c[1] and a[1] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif a[2] == b[2] == c[2] and a[2] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif a[3] == b[3] == c[3] and a[3] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif a[1] == b[2] == c[3] and a[1] == '0':
        print("Игра окончена! Нолики победили!")
        quit()
    elif a[3] == b[2] == c[1] and a[3] == '0':
        print("Игра окончена! Нолики победили!")
        quit()

def x_():
    x_goes()
    input_turn('x')
    game_over()

def o_():
    o_goes()
    input_turn('o')
    game_over()

def game():
    x_()
    o_()

print('Привет! Это экспериментальная версия игры крестики-нолики!')
print()
print('Для продолжения нажимайте Enter')
input()
print('Для начала объясню принцип игры:')
print('Чтобы сходить - нужно написать 2 числа через пробел.')
print('Первое число - номер строки сверху, от 1 до 3.')
print('А второе - номер столбика, идентично от 1 до 3 :)')
input()
print('Теперь выберите за кого вы будете играть)')
input()
print('А теперь давай играть!')
empty_board()
print()

MAX_TURNS = 9
for i in range(MAX_TURNS):
    game()

    