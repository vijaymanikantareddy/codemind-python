def ispalin(n):
    return str(n)==str(n)[::-1]
    
n = int(input())
a = n-1
b = n+1
l=[]
while(True):
    if(ispalin(a)):
        l.append(a)
    if(ispalin(b)):
        l.append(b)
    if(len(l)!=0):
        break
    a-=1
    b+=1

for i in l:
    print(i, end=' ')