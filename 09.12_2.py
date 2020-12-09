per = [int(i) for i in input().split()]
for i in range(1, len(per), 2):
    per[i - 1], per[i] = per[i], per[i - 1]
print(' '.join([str(i) for i in per]))