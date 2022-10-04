def fun(n):
    a = 1
    while(True):
        if(a*(a+1)==n):
            return True
        a +=1
        if(a*(a+1)>n):
            return False
            
n = int(input())
if fun(n):
    print('YES')
else:
    print("NO")