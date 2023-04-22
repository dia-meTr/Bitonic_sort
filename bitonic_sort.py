
def bitonic_sort(direction, arr):

    if len(arr) <= 1:
        return arr

    else:
        first = bitonic_sort(True, arr[:len(arr) // 2])
        second = bitonic_sort(False, arr[len(arr) // 2:])

        return bitonic_merge(direction, first + second)


def bitonic_merge(direction, arr):

    if len(arr) == 1:
        return arr
    else:

        bitonic_compare(direction, arr)
        first = bitonic_merge(direction, arr[:len(arr) // 2])
        second = bitonic_merge(direction, arr[len(arr) // 2:])
        return first + second


def bitonic_compare(direction, arr):

    dist = len(arr) // 2

    for i in range(dist):

        if (arr[i] > arr[i + dist]) == direction:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]
