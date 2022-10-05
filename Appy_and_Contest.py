def lcm(a,b):
    i=2
    s=1
    while i<a and i<b:
        if a%i==0 and b%i==0:
            s*=i
            a//=i
            b//=i
        else:
            i+=1
    return s*a*b

n = int(input())
for i in range(n):
    n,a,b,k = map(int, input().split())
    ac=n//a
    bc = n//b
    lc = lcm(a,b)
    abc = 2*(n//lc);
    if(ac+bc-abc>=k):
        print("Win")
    else:
        print("Lose")