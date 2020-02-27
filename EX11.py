a=input("Input a number : ")
b=range(2,int(a)-1)
c=0
for i in b:
    if int(a) % i == 0:
        c = c+1


if c != 0:
    print(str(a) + " is a non prime number")
else:
    print(str(a) + " is a prime number")
