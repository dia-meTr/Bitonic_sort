
def sort_checking(func, array, is_up, key, *args):
    array = func(is_up, array, key, *args)
    return sorted(array, key=key, reverse=not is_up) == array


def check_correction(func, random_lists, key=lambda x: x, *args):
    for random_list in random_lists:
        print(f"Sorting in ascending order {len(random_list)} elements ... ", end='')
        print(sort_checking(func, random_list, 1, key, *args))

        print(f"Sorting in descending order {len(random_list)} elements ... ", end='')
        print(sort_checking(func, random_list, 0, key, *args))
