a = int(input())
b = int(input())
for num in range(a, b+1):
    if str(num)==str(num)[::-1]:
        print(num, end=' ')