def isprime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

a=int(input())
b=int(input())
c=a+b+1
flag=1
while flag==1:
    if isprime(c):
        flag=0
    else:
        c=c+1
print(c-a-b)