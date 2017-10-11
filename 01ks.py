weight = [10, 20, 30]
vals =[60,100,120] 
memo = {}
def ks(n, W ):
    if n == 0 or W == 0:
        return 0
    elif (n,W) in memo:
        return memo[n,W]
    else:
        ans = max(ks(n-1,W), vals[n-1] + ks(n-1, W-weight[n-1]))
        memo[n,W] = ans
        return ans

print(ks(3,50))
