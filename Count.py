n = int(input())
arr = list(map(int, input().split()))
e = 0
od = 0
for ele in arr:
    if ele%2==0:
        e += 1
    else:
        od += 1
print(e, od)