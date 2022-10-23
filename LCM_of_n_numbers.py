def lcm(a, b):
    res = max(a,b)
    if res%a==0 and res%b==0:
        return res
    while res%a!=0 or res%b!=0:
        res += max(a, b)
    return res

n = int(input())
arr = list(map(int, input().split()))
res = arr[0]
for i in range(1, len(arr)):
    res = lcm(res, arr[i])
print(res)