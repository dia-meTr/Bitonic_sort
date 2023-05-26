import time
from Result import *


def calculate_time(func, result, random_list, is_up, key, *args):
    n = len(random_list)
    begin = time.time()

    func(is_up, random_list, key, *args)
    end = time.time()
    time_count = end - begin
    print(f"Total time of sorting {n} elements taken in : {time_count} seconds")

    result.add_time(time_count)


def run_time_calculation(func, results, random_list, is_up, processes=1, m_count=0, key=lambda x: x):
    n = len(random_list)
    res = Result(n, processes, m_count)
    results.append(res)

    for _ in range(0, 5):
        calculate_time(func, res, random_list, is_up, key, processes, m_count)

    print_results(results)


def print_results(results):
    print("{:<10} {:<4} {:<4} {:<17} {:<17}".format("Elements", "Threads", "Task", "Time", "Average time"))

    for res in results:
        res.print_res()