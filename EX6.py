s = input("please input your string : ")
l = len(s)
pal = 0
for i,j in zip(range(0, l-1), range(l-1, 0 , -1)):
    if s[i] != s[j]:
        print("This is not a palindrom string")
        pal = 1
        break
    
if pal == 0:
    print("This is a Palindrom String")
print("Program execution ends")
