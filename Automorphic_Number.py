def fun(n):
    sq = n*n
    a = len(str(n))
    b = 10**a
    c = sq%b
    return c==n

n = int(input())
if fun(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")