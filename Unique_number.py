def fun(n):
    n = str(n)
    li = {ch for ch in n}
    return len(n)==len(li)
    
n = int(input())
if fun(n):
    print('Unique Number')
else:
    print('Not Unique Number')