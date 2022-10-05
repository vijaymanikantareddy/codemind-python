n = int(input())
for i in range(1, n + 1):
    if i == n:
        print("*"*n)
    else:
        for j in range(1, n + 1):
            if j == 1 or j == i:
                print("*",end = "")
            else:
                print(" ",end = "")
    if i!=n:
        print("")