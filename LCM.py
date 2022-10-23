def lcm(a, b):
    res = max(a,b)
    if res%a==0 and res%b==0:
        return res
    while res%a!=0 or res%b!=0:
        res += max(a, b)
    return res

a, b = map(int, input().split())
print(lcm(a,b))