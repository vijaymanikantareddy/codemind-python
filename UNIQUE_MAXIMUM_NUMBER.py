n = int(input())
arr = list(map(int, input().split()))
se = {}
for ele in arr:
    if ele in se:
        se[ele] += 1
    else:
        se[ele] = 1
mx = -1
for k, v in se.items():
    if v==1:
        if mx < k:
            mx = k
print(mx)