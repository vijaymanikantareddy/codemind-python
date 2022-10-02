st = input()
arr = st.split(" ")
for word in arr:
    print(word[::-1], end=' ')