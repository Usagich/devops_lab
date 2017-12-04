from collections import defaultdict
d = defaultdict(list)

#count of words in A
A = int(raw_input())
#count of words in B
B = int(raw_input())
#step for comparing
step = int(raw_input())

resultList = []

for i in range(0, A):
    d['A'].append(str(i))
for i in range(0, B):
    d['B'].append(str(i))

for i in d.items():
    print i

for i in range(0, A, step):
    for j in range(0, B, step):
        if d['A'][i] == d['B'][j]:
            if j not in resultList:
                resultList.append(j)

print resultList