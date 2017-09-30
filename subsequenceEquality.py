from collections import Counter

ans = list()
for t in range(int(input(""))):

    c = Counter(input(""))

    for i in c.values():
        if i > 1:
            ans.append("yes")
            break
    else:
        ans.append("no")

for i in ans:
    print(i)
