import random
from apartment import Apartment, ApartmentSchema


def write_info(rand_func, file_name):
    with open(file_name, 'w') as f:
        for n in [65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]:
            for i in range(0, 1):
                a = rand_func(n)
                print(a)
                f.write(str(a) + '\n')


def rand_int(n):
    random_list = random.sample(range(0, 8388690), n)
    return random_list


def rand_float(n):
    random_list = []
    for _ in range(0, n):
        random_list.append(random.uniform(0, 8388690))

    return random_list


def rand_apartment(n):
    random_list = []
    for _ in range(0, n):
        random_list.append(Apartment())

    return random_list


if __name__ == "__main__":
    # write_info(rand_float, "data_float.txt")
    write_info(rand_int, "data.txt")
