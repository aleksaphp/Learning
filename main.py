# ___
# ___
# ___
# крестик ходи
# > 0 1
# нолик ходи
# > 0
# x__
# _x_
# __x
# крестик победил

def sum(list):
    res = 0
    for i in list:
        res += i
    return res

assert(sum([1, 2, 3]) == 6)
assert(sum([]) == 0)

# Крестик нолики ебать

Z = '_'
X = 'X'
O = 'O'



def changed_board(x, y):
    input(x, y)




def x_goes():
    return 'Крестик ходит'

def o_goes():
    return 'Нолик ходит'

def index(x, y):
    return x + y * 3

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[index(i, j)], end='')
        print()

a = ['_', '_', '_']
b = ['_', '_', '_']
c = ['_', '_', '_']

def empty_board():
    print(' '.join(a))
    print(' '.join(b))
    print(' '.join(c))
    return

print(empty_board)
