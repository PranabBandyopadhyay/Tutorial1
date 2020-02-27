a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
j = input("tell me a number : ")
for i in a:
    if int(i) >= int(j):
        b.append(i)

print(b)