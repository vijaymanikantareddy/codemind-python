def ispalin(n):
    s = str(n)
    return s==s[::-1]

def rev(n):
    n = str(n)[::-1]
    return int(n)

n = int(input())
while True:
    n += rev(n)
    if(ispalin(n)):
        break
print(n)