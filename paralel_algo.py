from datetime import datetime
from multiprocessing import Pool, cpu_count
import itertools
from bitonic_sort import bitonic_merge, bitonic_sort
from math import log2


def time_counter(array, is_up):
    print()
    n = len(a)

    time1 = datetime.now()

    array = sort(array, is_up)

    time2 = datetime.now()

    print(sorted(array) == array)
    print("Current Time =", time2 - time1)

    if results.get(n) is None:
        results[n] = [(time2 - time1).total_seconds()]
    else:
        results[n].append((time2 - time1).total_seconds())


def get_args(array, n, m, is_up):
    args = []
    i = 0

    while i < n:
        if (i / m) % 2 == 0:
            args.append((is_up, array[i:i + m]))
        else:
            args.append((not is_up, array[i:i + m]))
        i = i + m

    return args


def sort(array, is_up):
    n = len(array)
    processes = 2 ** round(log2(cpu_count() * 5))
    m = n // processes

    pool = Pool(processes=processes)
    args = get_args(array, n, m, is_up)
    outputs = pool.starmap(bitonic_sort, args)

    array = list(itertools.chain(*outputs))

    while m <= n:
        m = m * 2
        args = get_args(array, n, m, is_up)
        outputs = pool.starmap(bitonic_merge, args)
        array = list(itertools.chain(*outputs))

    return array


if __name__ == "__main__":
    up = 1
    results = {}
    lists = []

    with open('data.txt') as f:
        for i in range(0, 9):
            line = f.readline()
            a = line[1:-2].split(', ')
            a = list(map(int, a))
            lists.append(a)

        for a in lists:
            time_counter(a, up)


