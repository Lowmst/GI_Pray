import random


def pray(info):
    S_count = info['S_count']
    A_count = info['A_count']
    non_UP_count = info['non_UP_count']

    if S_count < 74:
        S_weight = 6
    elif 73 < S_count < 90:
        S_weight = 6 + 60 * (S_count - 73)
    else:
        S_weight = 1000

    if A_count < 9:
        A_weight = 51
    elif 8 < A_count < 10:
        A_weight = 51 + 510 * (A_count - 8)
    else:
        A_weight = 1000

    pool = [0 for _ in range(1000)]
    for i in range(S_weight):
        pool[i] = 2
    for i in range(A_weight):
        if i + S_weight >= 1000:
            break
        pool[i + S_weight] = 1

    result_init = pool[random.randint(0, 999)]
    if result_init == 0:
        S_count += 1
        A_count += 1
        info['S_count'] = S_count
        info['A_count'] = A_count
        return 'B'
    elif result_init == 1:
        S_count += 1
        A_count = 0
        info['S_count'] = S_count
        info['A_count'] = A_count
        return 'A'

    elif result_init == 2:
        S_count = 0
        A_count += 1
        info['S_count'] = S_count
        info['A_count'] = A_count

        UP_weight = 5 + non_UP_count
        UP_pool = [0 for _ in range(10)]
        for i in range(UP_weight):
            UP_pool[i] = 1

        result_next = UP_pool[random.randint(0, 9)]
        if result_next == 1:
            non_UP_count = 0
            info['non_UP_count'] = non_UP_count
            return 'S+'
        elif result_next == 0:
            non_UP_count += 1
            info['non_UP_count'] = non_UP_count
            return 'S-'

num = 100000

inner_info = {
    'S_count': 0,
    'A_count': 0,
    'non_UP_count': 0,
}

record = []
for i in range(num):
    record.append(pray(inner_info))


S_record = []
for i in record:
    if i == 'S+' or i == 'S-':
        S_record.append(i)
print(S_record)


UP_record = []
non_UP_record = []
for i in record:
    if i == 'S+':
        UP_record.append(i)
    elif i == 'S-':
        non_UP_record.append(i)

print(len(UP_record))
print(len(non_UP_record))
print(len(UP_record)/(len(UP_record)+len(non_UP_record)))