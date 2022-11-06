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

    h = int(n*0.0001)
    r = v[-1] - v[0]
    per = int((x-v[0]) / r * n) if int(x / r * n) <= n-1 else n-1
    der = per + h if per + h < n-1 else n-1
    izq = per - 2*h if per - 2*h > 0 else 0

    try:
        if v[der] < x:
            izq = der
            der = der + 2*h if der + 2*h <= n-1 else n-1
        elif v[izq] > x:
            der = izq
            izq = izq - 2*h if izq - 2*h >= 0 else 0
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
    n = 10_000_000
    v = np.array(sorted(set(np.random.randint(0, n*10, n))))

    serched_value = random.choice(v)
    index, cont = new_binary_search(v, serched_value)

    print(index, serched_value, cont)


if __name__ == '__main__':
    test()
