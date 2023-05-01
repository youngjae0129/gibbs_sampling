import pandas as pd
import numpy as np

f = open('vocab.txt', 'r')
vocabs = []
while True:
    line = f.readline().strip()
    vocabs.append(line)
    if line == 'buffs': break
f.close()
f = open('ap.dat', 'r')
data = pd.DataFrame(columns=vocabs)
for _ in range(2246):
    line = f.readline()
    row = [0] * 10473
    for str in line.strip().split(' '):
        if ':' in str:
            str_split = str.split(':')
            row[int(str_split[0])] = int(str_split[1])
    data.loc[len(data)] = row
f.close()
z = np.random.randint(0, 5, size=2246)
data['z'] = z
data.to_csv('data.csv')