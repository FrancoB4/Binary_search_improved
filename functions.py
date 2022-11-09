import random
import numpy as np


def binary_search(v, x, cnt=0):
    der = len(v) - 1
    izq = 0

    cont = 0 + cnt

    while izq <= der:
        c = (der + izq) // 2
        cont += 1

        if v[c] == x:
            return c, cont
        elif x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1, cont


def new_binary_search(v, x, default_vector=None, cnt=0):
    cont = 0 + cnt
    n = len(v)

    if default_vector is None:
        df = v
    else:
        df = default_vector

    if n == 0 or v[0] > x or x > v[-1]:
        return -1, cont

    sector_len = int(n*0.0001)
    vector_range = v[-1] - v[0]
    target_sector = int((x-v[0]) / vector_range * n) if int(x / vector_range * n) <= n-1 else n-1
    right = target_sector + sector_len if target_sector + sector_len < n-1 else n-1
    left = target_sector - 2*sector_len if target_sector - 2*sector_len > 0 else 0

    try:
        if v[right] < x:
            left = right
            right = right + 2*sector_len if right + 2*sector_len <= n-1 else n-1
        elif v[left] > x:
            right = left
            left = left - 2*sector_len if left - 2*sector_len >= 0 else 0
    except IndexError as ie:
        print(ie)
        print(f'Right:          {right}\n'
              f'Left:           {left}\n'
              f'n:              {n}'
              f'Target Sector:  {target_sector}')

    while left <= right:
        c = (right + left) // 2
        cont += 1

        try:
            if v[c] == x:
                return c, cont
            elif x < v[c]:
                right = c - 1
            else:
                left = c + 1
        except IndexError:
            raise IndexError(f'El indice [{c}] esta fuera del rango de la lista [{n}] los parámetros actuales fueron:\n'
                             f'Right;           {right}\n'
                             f'Left:            {left}\n'
                             f'Operations:      {cont}\n'
                             f'Sector Len:      {sector_len}\n'
                             f'Vector Range:    {vector_range}')

    if left > x:
        return binary_search(df, x)
    return binary_search(df, x)


def test():
    n = 10_000_000
    v = np.array(sorted(set(np.random.randint(0, n*10, n))))

    serched_value = np.random.choice(v)
    index, cont = new_binary_search(v, serched_value)

    print(index, serched_value, cont)


if __name__ == '__main__':
    test()
