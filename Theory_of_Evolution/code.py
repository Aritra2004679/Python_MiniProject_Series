# File Handling , Random module (Pre-requisites)

import random

def evolve(x):
    idx = random.randint(0, len(x) - 1)
    p = random.randint(1, 100)

    print(p)

    # Mutation probability = 1%
    if p == 1:
        if x[idx] == '0':
            x[idx] = '1'
        else:
            x[idx] = '0'


with open("dna_data.txt") as myfile:
    x = myfile.read()

x = list(x)

for i in range(0, 10000):
    evolve(x)

print("\nFinal DNA Sequence:")
print(''.join(x))