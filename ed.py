import time as t 
memo = {}
def ed(a, b, m, n):
    if (m, n) in memo:
        return memo[m, n]
    else:
        if m == 0 and n == 0 :
            return 0
        if m == 0 or n == 0:
            return max(m, n)
        c = 0 if a[m-1] == b[n-1] else 1
        #print("here")
        a =  min(1 + ed(a, b, m-1, n), 1 + ed(a, b, m, n-1), c + ed(a, b, m-1, n-1))
        memo[m, n] = a
        return a

a = 'lamps'
b = 'Mathematica'
before = t.time()
ans = ed(a, b, len(a), len(b))
after = t.time()
print(ans," took {}s".format(after-before))
