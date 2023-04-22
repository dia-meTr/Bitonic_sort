from datetime import datetime
from sorting_techniques import pysort

sortObj = pysort.Sorting()

def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]


def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)


def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)


def sort(a, up):
    n = len(a)
    time1 = datetime.now()
    bitonicSort(a, 0, n, up)
#    sortResult = sortObj.heapSort(a)

    time2 = datetime.now()
    # print("\nCurrent Time =", time2 - time1)
    if results.get(n) is None:
        results[n] = [(time2 - time1).total_seconds()]
    else:
        results[n].append((time2 - time1).total_seconds())


up = 1
results = {}
with open('data.txt') as f:
    for i in range(0, 3):
        line = f.readline()
        a = line[1:-2].split(', ')
        a = list(map(int, a))

        sort(a, up)

for key, value in results.items():
    print(f'{key}  -  {round(sum(value)/3, 4)}  -  {value}')
