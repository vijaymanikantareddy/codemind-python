n = int(input())
arr = list(map(int, input().split()))
su = 0
for ele in arr:
    ab = int(ele**0.5)
    if ab*ab == ele:
        su += ele
print(su)