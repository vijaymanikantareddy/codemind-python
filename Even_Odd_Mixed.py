def fun(n):
    li = [int(ch) for ch in str(n)]
    even = False
    odd = False
    for i in li:
        if i%2==0:
            even = True
        else:
            odd = True
    if even and odd:
        return "Mixed"
    elif even:
        return "Even"
    else:
        return "Odd"
    
n = int(input())
print(fun(n))