n = int(input())
arr = list(map(int, input().split()))
dic = {}
for ele in arr:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1
mx = arr[0]
mx_cnt = dic[arr[0]]
for k, v in dic.items():
    if mx_cnt < v:
        mx_cnt = v
        mx = k
    if mx_cnt == v:
        mx = min(mx, k)
print(mx)