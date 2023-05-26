from datetime import datetime
from bitonic_sort import bitonic_sort


def sort(array, is_up):
    n = len(array)

    time1 = datetime.now()

    array = bitonic_sort(is_up, array)

    time2 = datetime.now()

    print(sorted(array) == array)
    print("Current Time =", time2 - time1)

    if results.get(n) is None:
        results[n] = [(time2 - time1).total_seconds()]
    else:
        results[n].append((time2 - time1).total_seconds())


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
            sort(a, up)

    for key, value in results.items():
        print(f'{key}  -  {round(sum(value) / 3, 4)}  -  {value}')

