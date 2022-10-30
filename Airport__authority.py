n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
t = int(input())
res = 0
for ele in arr:
    if ele>t:
        res += 2
    else:
        res += 1
print(res)