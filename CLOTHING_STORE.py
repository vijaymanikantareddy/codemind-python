n = int(input())
arr = list(map(int, input().split()))[:n]
dic = {}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
res = 0
for key, val in dic.items():
    res += val//2
print(res)