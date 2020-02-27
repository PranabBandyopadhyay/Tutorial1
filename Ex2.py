var = input("Enter a number: ")

div = int(var) % 2

if var == 0:
    print("0 is neither Odd nor Even")
elif div == 1:
    print(str(var) + " is an Odd number.")
else:
    print(str(var) + " is an Even number.")