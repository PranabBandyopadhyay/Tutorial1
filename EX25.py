user_num = input("Guess a number of your choiche between 1 to 100: ")

not_found = True

def mid(a, b):
    return round(a+((b-a)/2))
a=1
b=100

while not_found:
    c=mid(a, b)
    choice = int(input("Is your number " + str(c) + " ? (1 for too high, 2 for too low, 3 for ok)"))
    if choice == 1:
        b=c
    elif choice == 2:
        a=c
    elif choice ==3:
        print("Your number is " + str(c))
        break




