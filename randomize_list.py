import random


with open("data.txt", 'w') as f:
    for n in [65536, 131072, 262144]:
        for i in range(0, 3):
            a = random.sample(range(10, 362144), n)
            print(a)
            f.write(str(a) + '\n')
