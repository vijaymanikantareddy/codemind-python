a = int(input())
res=1
for i in range(2, a//2+1):
    if(a%i==0):
        if(i!=a//i):
            res+=i
        else:
            res+=i+a//i
print(res>=a)