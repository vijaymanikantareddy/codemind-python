def isvow(c):
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
        return True
    return False
    
def fun(s):
    res=""
    for i in s:
        if isvow(i):
            res +="V"
        else:
            res+="C"
       
    last = res[0];
    for i in range(1, len(res)):
        if(res[i]!=res[i-1]):
            last+=res[i]
    print(last)
     
st = input()
fun(st)