import numpy as np
count = []
lines = 0
with open('training.txt','r', encoding= 'utf8') as f:
    for line in f:
        count.append(len(line.split())-1)
        lines += 1

print(np.sort(count), lines)


