n = int(input())
counts = dict()
for i in range(n):
    m = int(input())
    if m in counts.keys():
        counts[m] += 1
    else :
        counts[m] = 1

maxx = 0
l = []
for i,j in counts.items():
    if j>maxx :
        maxx = j
        l = [i]
    elif j ==maxx:
        l += [i]
    else :
        pass
print(sorted(l))



