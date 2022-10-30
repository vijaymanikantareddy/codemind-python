t = int(input())
for _ in range(t):
    a = input()
    arr = [int(ele) for ele in a]
    b = True
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if abs(arr[i-1]-arr[i]) != 1:
            b = False
    if b:
        print("YES")
    else:
        print("NO")