import random
a = random.randint(1,9)
print("Enter quit anytime to quit.")
inp = "none"
while inp != "quit":
    inp = input("Enter You Guess : ")
    if inp.lower() == "quit":
        print("Thanks playing. The number was :" + str(a))
        break
    else:
        if int(inp) > a:
            print("You Guessed High")
        elif int(inp) < a:
            print("You Guessed Low")
        else:
            print("Good Job. You Guessed Right... Quitting")
            break