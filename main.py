# importing libraries
import json
import csv
from Result import Result
from paralel_algo import *
from randomize_list import rand_apartment
from correction_tests import *
from time_measurement import *
from apartment import *


def get_data(file_name, type_elements):
    random_lists = []

    with open(file_name) as f:
        for i in range(0, 8):
            line = f.readline()
            a = line[1:-2].split(', ')
            a = list(map(type_elements, a))
            random_lists.append(a)

    return random_lists


def get_json_data(file_name):
    random_lists = []

    with open(file_name) as file:
        for line in file.readlines():
            data = json.loads(line)
            ApartmentSchema(many=True).load(data)

    return random_lists


def research_parameters(func, random_list, is_up, file_name, key):
    n = len(random_list)
    results = []
    processes_counts = [2, 4, 6, 8]
    params = [2 ** j for j in range(2, round(log2(8)))]
    print(params)
    for processes_count in processes_counts:
        for task_size in params:
            res = Result(n, processes_count, task_size)
            results.append(res)
            for j in range(3):
                calculate_time(func, res, random_list, is_up, key, processes_count, task_size)

        print_results(results)

    res = Result(n)
    calculate_time(bitonic_sort, res, random_list, is_up, key)
    res_to_csv(results, file_name, random_list, is_up, key)


def res_to_csv(results, file_name, random_list, is_up, key):
    res = []
    run_time_calculation(bitonic_sort, res, random_list, is_up, key=key)
    seq_time = res[0].count_average_time()

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        for r in results:
            writer.writerow(r.get_info(seq_time))
        writer.writerow(res[0].get_info(seq_time))


def key_base(x):
    return x


def key_price(x):
    return x.price


def key_area(x):
    return x.area


def key_rate(x):
    return x.rate


def apartment_sorting():
    # TEST APARTMENT SORTING
    # check_correction(bitonic_sort, lists, lambda x: x.price)
    for i in range(20, 24):
        rand_list = rand_apartment(2 ** i)
        # check_correction(parallel_sort, [rand_list], key_price, 8, 8)
        run_time_calculation(parallel_sort, results, rand_list, 1, 8, 8, key_price)
        res_to_csv(results, "exp_apartment", rand_list, 1, key_price)


def sort_test():
    # TEST SORTING
    lists = get_data('data_float.txt', float)
    for rand_list in lists[5:]:
        print(len(rand_list))
        # check_correction(bitonic_sort, lists, lambda x: x)
        # check_correction(parallel_sort, [rand_list], key_price, 8, 8)
        run_time_calculation(parallel_sort, results, rand_list, 1, 8, 8, key=key_base)
        res_to_csv(results, "exp_apartment", rand_list, 1, key=key_base)


def run_research():
    pass


if __name__ == "__main__":
    results = []

    l = [6, 3, 8, 4, 1, 2, 5, 7]
    research_parameters(parallel_sort, l, 1, f'test1.csv', key_base)

    #lists = get_data('data.txt', float)
    #for l in lists:
    #    research_parameters(parallel_sort, l, 1, f'exp6cores.csv', key_base)


