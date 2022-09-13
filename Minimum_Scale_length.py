def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)
        
n = int(input())
a = list(map(int, input().split()))[:n]
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)