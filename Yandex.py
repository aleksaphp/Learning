import string

N = int(input())
final_decision = []

for i in range(1, N+1):
    inf = input()
    inf_list = inf.rsplit(',')

    f = ''.join(inf_list[0])
    i = ''.join(inf_list[1])
    o = ''.join(inf_list[2])
    d = ''.join(inf_list[3])
    m = ''.join(inf_list[4])
    y = ''.join(inf_list[5])

    fio_list = inf_list[0], inf_list[1], inf_list[2]
    fio = ''.join(fio_list)
    fio_amount = len(set(fio))

    d_list = [int(a) for a in str(d)]
    m_list = [int(a) for a in str(m)]
    if len(d_list) == 2:
        d_list_sum = d_list[0] + d_list[1]
    else:
        d_list_sum = int(d)

    if len(m_list) == 2:
        m_list_sum = m_list[0] + m_list[1]
    else:
        m_list_sum = int(m)

    dm_sum = d_list_sum + m_list_sum
    
    f_list = list(f)
    alphabet = list(string.ascii_uppercase)
    alphabet_num = alphabet.index(f_list[0])+1
    
    puzzle = fio_amount + dm_sum * 64 + alphabet_num * 256
    puzzle_16 = f'{puzzle:x}'
    puzzle_16_rev = puzzle_16[::-1]
    puzzle_16_rev = list(puzzle_16_rev) 
    puzzle_list = puzzle_16_rev[2], puzzle_16_rev[1], puzzle_16_rev[0]
    puzzle_decision = ''.join(puzzle_list)

    final_decision.append(puzzle_decision)


print(' '.join([str(i).upper() for i in final_decision]))
    







