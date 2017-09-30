memo = {}
def lss(a, b):
    m = len(a)
    n = len(b)
    #print('looking at {}   and   {}'.format(a, b))
    if (m, n) in memo:
       # print("\tTime saved! for ({}, {})".format(m, n))
        return memo[(m,n)]
    else:
        #print('\tcomputing from sccratch for :   ({},{})'.format(m,n))
        if m == 0 or n == 0:
            ans = 0
        elif a[m-1] == b[n-1]:
            ans = 1 + lss(a[ : m - 1], b[ : n - 1])
        else:
            ans =  max(lss(a, b[ : n - 1]), lss(a[ : m - 1], b))
        memo[(m,n)] = ans
        #print("\tmemoized ({}, {})".format(m, n))
        return ans
import time as t

before = t.time()
ans = lss("miilolopantion", "loganis")
after = t.time()

print(ans, " took {}s".format(after - before))
