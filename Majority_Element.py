n = int(input())
arr = list(map(int, input().split()))
di = {}
for ele in arr:
    if ele in di:
        di[ele] += 1
    else:
        di[ele] = 1
mx = 0
mxnum = arr[0]
for k,v in di.items():
    if mx < v:
        mx = v
        mxnum = k
print(mxnum)