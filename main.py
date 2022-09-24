from functions import *
import numpy as np


def test():
    n = 1000000
    cont = [0] * 4
    iterations = [0] * 2
    time_counter = {'bs': 0, 'nbs': 0}
    v = np.array(sorted(set(np.random.randint(0, n*10, n))))

    for i in range(n):
        serched_value = random.choice(v)

        bs_time_start = time.time()
        index_bs = binary_search(v, serched_value)
        bs_time_end = time.time()

        time_counter['bs'] += bs_time_end - bs_time_start
        iterations[0] += index_bs[1]

        nbs_time_start = time.time()
        index_nbs = second_new_binary_search(v, serched_value)
        nbs_time_end = time.time()

        time_counter['nbs'] += nbs_time_end - nbs_time_start
        iterations[1] += index_nbs[1]

        if index_nbs[0] != index_bs[0]:
            cont[0] += 1
        elif index_nbs[0] == index_bs[0]:
            if index_nbs[1] < index_bs[1]:
                cont[1] += 1
            elif index_nbs[1] == index_bs[1]:
                cont[2] += 1
            else:
                cont[3] += 1

        # print(index_bs[0], index_nbs[0])

    print(f'Binary Search Total Time:           {time_counter["bs"]}\n'
          f'New Binary Search Total Time:       {time_counter["nbs"]}')

    better = round(cont[1] / n * 100, 2)
    worst = round(cont[3] / n * 100, 2)
    equals = round(cont[2] / n * 100, 2)
    bad = round(cont[0] / n * 100, 2)

    print(f'Times NBS made less iterations than BS:                 {cont[1]} ({better}%)\n'
          f'Times BS made less iterations than NBS:                 {cont[3]} ({worst}%)\n'
          f'Times BS made the same amount of iterations than NBS:   {cont[2]} ({equals}%)\n'
          f'Times NBS works bad:                                    {cont[0]} ({bad}%)')

    print(f'Mean Iterations BS:     {round(iterations[0]/n, 2)} Iterations\n'
          f'Mean Iterations NBS:    {round(iterations[1]/n, 2)} Iterations')


if __name__ == '__main__':
    test()
