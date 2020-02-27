a=input("Input a number : ")
b=range(1,int(a))
print("List of Divisors of " + a + " are : ")
for i in b:
    if int(a) % i == 0:
        print(i)
