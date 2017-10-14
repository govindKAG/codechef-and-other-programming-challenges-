#a = [1, -1, 2, 3, -1, 8]
a = [1, -1, 2, 3,-1]
#for max subsequence, not necessarily contiguous  
def mss(n):
    if n == 0:
        return a[n]
    else:
        return max(a[n] + mss(n-1), mss(n-1))
#for max subarray , still buggy 
def msa(n):
    if n == 0:
        return a[n]
    else:
        return max(a[n], a[n] + msa(n-1))

print(mss(len(a) - 1)) 
print(msa(len(a) - 1)) 
