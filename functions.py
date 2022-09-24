import random
import time
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


def new_binary_search(v, x, mod=0, cnt=0):
    cont = 0 + cnt
    n = len(v)
    if v[0] > x or x > v[-1]:
        return -1, cont

    h = int(n / 11)
    r = v[-1] - v[0]
    per = int(x / r * 10)
    der = h * (per + 1 + mod)
    izq = der - 2*h

    if der < x:
        if der + h <= n:
            der = der + h
            izq = izq + h
        else:
            der = n - 1
            izq = der - h
    elif izq > x:
        if izq - h >= 0:
            izq = izq - h
            der = der - 2 * h
        else:
            izq = 0
            der = h

    while izq <= der:
        c = (der + izq) // 2
        cont += 1

        if v[c] == x:
            return c, cont
        elif x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    # if izq > x:
    #     return new_binary_search(v, x, mod=-1 + mod, cnt=cont)
    # return new_binary_search(v, x, mod=1 + mod, cnt=cont)
    return binary_search(v, x, cnt=cont)


def second_new_binary_search(v, x, default_vector=None, cnt=0):
    cont = 0 + cnt
    n = len(v)

    if default_vector is None:
        df = v
    else:
        df = default_vector

    if n == 0 or v[0] > x or x > v[-1]:
        return -1, cont
    # try:
    #     if v[0] > x or x > v[-1]:
    #         return binary_search(default_vector, x)
    # except IndexError or ValueError:
    #     raise IndexError(f'El rango de la lista es [{n}]; los parámetros actuales fueron:\n'
    #                      f'Iteraciones:         {cont}\n')

    lr = 1/(n*.001)
    h = int(n*lr)
    r = v[-1] - v[0]
    per = int((x-v[0]) / r * n) if int(x / r * n) <= n-1 else n-1
    der = per + h if per + h < n-1 else n-1
    izq = per - 2*h if per - 2*h > 0 else 0

    # print(f'-'*40, '\n',
    #       f'n: {n}\n'
    #       f'v[0]: {v[0]}\n'
    #       f'v[-1]: {v[-1]}\n'
    #       f'lr: {lr}\n'
    #       f'h: {h}\n'
    #       f'per: {per}\n'
    #       f'der: {der}\n'
    #       f'izq: {izq}\n'
    #       f'x: {x}\n'
    #       f'r: {r}\n'
    #       f'index: {list(v).index(x)}\n'
    #       f'v_ {v}')

    try:
        if v[der] < x:
            izq = der
            der = der + 2*h if der + 2*h <= n-1 else n-1
            # return second_new_binary_search(v[der:], x, default_vector=df, cnt=cont+1)
        elif v[izq] > x:
            der = izq
            izq = izq - 2*h if izq - 2*h >= 0 else 0
            # return second_new_binary_search(v[:izq], x, default_vector=df, cnt=cont+1)
    except IndexError as ie:
        print(ie)
        print(f'Derecha:    {der}\n'
              f'Izquierda:  {izq}\n'
              f'n:          {n}'
              f'per:        {per}')

    while izq <= der:
        c = (der + izq) // 2
        cont += 1

        try:
            if v[c] == x:
                return c, cont
            elif x < v[c]:
                der = c - 1
            else:
                izq = c + 1
        except IndexError:
            raise IndexError(f'El indice [{c}] esta fuera del rango de la lista [{n}] los parámetros actuales fueron:\n'
                             f'Derecha;             {der}\n'
                             f'Izquierda:           {izq}\n'
                             f'Iteraciones:         {cont}\n'
                             f'Longitud del salto:  {h}\n'
                             f'Rango:               {r}')

    if izq > x:
        return binary_search(df, x)
    return binary_search(df, x)


def test():
    n = 10000000
    v = np.array(sorted(set(np.random.randint(0, n*10, n))))

    serched_value = random.choice(v)
    index, cont = second_new_binary_search(v, serched_value)

    print(index, serched_value, cont)

    # acum = [None] * n
    # tiempo_total = 0
    #
    # for i in range(n):
    #     serched_value = random.choice(v)
    #
    #     start = time.time()
    #     nbs_index = second_new_binary_search(v, serched_value)
    #     end = time.time()
    #
    #     tiempo_total += end-start
    #     acum[i] = nbs_index[0]
    #
    # print(acum)
    # print(tiempo_total)


if __name__ == '__main__':
    test()
