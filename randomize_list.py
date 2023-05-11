import random


with open("data.txt", 'w') as f:
    for n in [262144, 131072, 65536]:
        for i in range(0, 3):
            a = random.sample(range(0, 362144), n)
            print(a)
            f.write(str(a) + '\n')
