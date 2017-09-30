def prefixSum(i,l):
    return sum(l[:i])

def suffixSum(i,l):
    return sum(l[i-1:])

def minSP(l,N):
    mins = dict()
    for i in range(1,N + 1):
        mins[i] = prefixSum(i,l) + suffixSum(i,l)
    return min(mins, key = mins.get)


times = int(input(""))
ans = []
inps = []
for t in range(times):
    N = int(input(""))
    l = input("")
    l = list(map(int,list(l.split(" "))))
    inps.append(l)


for i in inps:
    print(minSP(i,len(i)))
