def max_function(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


a = int(input("Please enter 1st number : "))
b = int(input("Please enter 2nd number : "))
c = int(input("Please enter 3rd number : "))

print("Largest number is : " +  str(max_function(a,b,c)))