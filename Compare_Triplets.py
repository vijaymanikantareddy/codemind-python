a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = 0
sb = 0
for i in range(len(a)):
    if a[i]>b[i]:
        sa += 1
    elif a[i]<b[i]:
        sb += 1
print(sa, sb)