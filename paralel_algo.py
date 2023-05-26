from multiprocessing import Pool, cpu_count
import itertools
from bitonic_sort import bitonic_merge, bitonic_sort
from math import log2


def get_args(array, n, m, is_up, comp_func):
    args = []
    j = 0

    while j < n:
        if (j / m) % 2 == 0:
            args.append((is_up, array[j:j + m], comp_func))
        else:
            args.append((not is_up, array[j:j + m], comp_func))
        j = j + m

    return args


def parallel_sort(is_up, array, key, processes, m_count):
    n = len(array)
    processes = 2 ** round(log2(processes))

    m = n // m_count

    pool = Pool(processes=processes)
    args = get_args(array, n, m, is_up, key)
    outputs = pool.starmap(bitonic_sort, args)

    array = list(itertools.chain(*outputs))

    while m <= n:
        m = m * 2
        args = get_args(array, n, m, is_up, key)
        outputs = pool.starmap(bitonic_merge, args)
        array = list(itertools.chain(*outputs))

    return array
