c=[1,1]
def fibo(a,b):
    c.append(a+b)
    return a+b

a=1
b=1
inp=input("How many in fibonacci series?: ")
if int(inp) == 0:
    print("No fibonacci series to print")
elif int(inp) == 1:
    print("You Fibonacci series is : " + str(c[0]))
else:
    for i in range(1,int(inp)-1):
        b,a=fibo(a,b),b
    print("You Fibonacci series is : " + str(c))