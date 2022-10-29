n = int(input())
arr = list(map(int, input().split()))
t = int(input())
t = t%n
for ele in arr[n-t:]:
    print(ele, end=' ')
for ele in arr[:n-t]:
    print(ele, end=' ')
