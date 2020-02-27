import random

num = str(random.randint(1, 9999)).zfill(4)
print(num)
inp = "0000"

class counter:
    def __init__(self, i):
        self.i = i
        self.cow_count = 0
        self.bull_count = 0

    def cow(self):
        a = [i for i in str(num)]
        b = [i for i in str(self.i)]
        for i,j in zip(range(0, len(a)), range(0, len(b))):
            print(i)
            print(j)
            if a[i] == b[j]:
                self.cow_count = self.cow_count + 1
                a[i] = i*"x"
                b[j] = i*"x"
        for i in range(0, len(a)):
            for j in range(0, len(b)):
                if a[i] == b[j] and i != j:
                    self.bull_count = self.bull_count+1


while inp != num:
    inp = input("Please enter your guess : ")
    
    if inp != num:
        c = counter(inp)
        c.cow()
        print("You have " + str(c.cow_count) + " cows and " + str(c.bull_count) + "bulls")

    else:
        print("You guessed correct")

