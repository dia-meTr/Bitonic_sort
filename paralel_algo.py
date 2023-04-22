from datetime import datetime
import numpy as np
from sorting_techniques import pysort
from multiprocessing import Pool, Manager, Array, cpu_count
from copy import copy

# Creating the Sort Object
sortObj = pysort.Sorting()


def compAndSwap(a, i, j, dire):
    ai = a[i]
    aj = a[j]

    if (dire == 1 and ai > aj) or (dire == 0 and ai < aj):
        a[i], a[j] = a[j], a[i]


def bitonicMerge(a, low, cnt, dire, limit):
    if cnt > limit:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire, limit)
        bitonicMerge(a, low + k, k, dire, limit)


def bitonicSort(l, low, cnt, dire, limit):
    if cnt > limit:
        print(cnt)
        k = cnt // 2
        bitonicSort(a, low, k, 1, limit)
        bitonicSort(a, low + k, k, 0, limit)
        bitonicMerge(a, low, cnt, dire, limit)
        return l


def sort1(a, up):
    n = len(a)
    numThreads = cpu_count() * 2
    print(numThreads)
    m = n / numThreads

    time1 = datetime.now()

    args = []
    i = 2
    j = 0

    while i <= m:
        while j < n:
            if (j / i) % 2 == 0:
                args.append((a, j, i, up))
                print(f"(a, {j}, {i}, {up})")
            else:
                args.append((a, j, i, not up))
                print(f"(a, {j}, {i}, {not up})")
            j = j + i

        i = i * 2

    print(a)
    print(args)

    with Pool(numThreads) as p:
        p.starmap(bitonicSort, args)
        p.close
        p.join

    time2 = datetime.now()
    print("\nCurrent Time =", time2 - time1)
    print(a)
    if results.get(n) is None:
        results[n] = [(time2 - time1).total_seconds()]
    else:
        results[n].append((time2 - time1).total_seconds())


def time_counter(up):
    n = len(a)
    time1 = datetime.now()
    sort(up)

    time2 = datetime.now()
    print("\nCurrent Time =", time2 - time1)
    print(a)
    if results.get(n) is None:
        results[n] = [(time2 - time1).total_seconds()]
    else:
        results[n].append((time2 - time1).total_seconds())


def custom_callback(result_iterable):
    # iterate results
    for result in result_iterable:
        print(f'Got result: {result}')


def sort(up):
    n = len(a)
    numThreads = cpu_count() * 2
    m = n // numThreads
    print(numThreads)
    print(m)

    args = []
    i = 0
    j = 0
    m_old = 1

    while m <= n:
        args.append([])
        while i < n:
            if (i / m) % 2 == 0:
                args[j].append((copy(a[i:i + m]), 0, m, up, m_old))
                print(f"(a[{i}:{i + m}], {0}, {m}, {up}, {m_old})")
            else:
                args[j].append((copy(a[i:i + m]), 0, m, not up, m_old))
                print(f"(a[{i}:{i + m}], {0}, {m}, {not up}, {m_old})")
            i = i + m
        j += 1
        # m_old = 1
        m = m * 2
        i = 0

    with Pool(numThreads) as p:
        print("--")
        #for i in range(0, 1):
        _ = p.starmap_async(bitonicSort, args[i], callback=custom_callback)

        p.close

        p.join

        print(i)


up = 1
results = {}

if __name__ == "__main__":
    with open('data.txt') as f:
        for i in range(0, 1):
            line = f.readline()
            a = line[1:-2].split(', ')
            a = list(map(int, a))
            # a = Array("i", list(map(int, a)))
            # print(a)

        with Manager() as m:
            l = m.list(a)
            time_counter(up)
