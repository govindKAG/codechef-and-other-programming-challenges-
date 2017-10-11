weight = [10, 20, 30]
vals =[60,100,120] 
def ks(n, W ):
    if n == 0 or W == 0:
        return 0
    else:
        return max(ks(n-1,W), vals[n-1] + ks(n-1, W-weight[n-1]))

print(ks(3,50))
