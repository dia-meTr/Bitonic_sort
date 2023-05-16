
def bitonic_sort(direction, arr, key=lambda x: x, *args):

    if len(arr) <= 1:
        return arr

    else:
        first = bitonic_sort(True, arr[:len(arr) // 2], key)
        second = bitonic_sort(False, arr[len(arr) // 2:], key)

        return bitonic_merge(direction, first + second, key)


def bitonic_merge(direction, arr, key=lambda x: x):

    if len(arr) == 1:
        return arr
    else:

        bitonic_swap(direction, arr, key)
        first = bitonic_merge(direction, arr[:len(arr) // 2], key)
        second = bitonic_merge(direction, arr[len(arr) // 2:], key)
        return first + second


def bitonic_swap(direction, arr, key):

    dist = len(arr) // 2

    for i in range(dist):

        if (key(arr[i]) > key(arr[i + dist])) == direction:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]



