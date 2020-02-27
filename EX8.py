class RPS:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play(self):
        if self.p1 == "rock" and self.p2 == "scissors":
            print("Rock beats scissors. Player1 wins.")
        elif self.p1 == "scissors" and self.p2 == "paper":
            print("Scissors beats paper. Player1 wins.")
        elif self.p1 == "paper" and self.p2 == "rock":
            print("Paper beats rock. Player1 wins.")
        elif self.p1 == "scissors" and self.p2 == "rock":
            print("Rock beats scissors. Player2 wins.")
        elif self.p1 == "paper" and self.p2 == "scissors":
            print("Scissors beats paper. Player2 wins.")
        elif self.p1 == "rock" and self.p2 == "paper":
            print("Paper beats rock. Player2 wins.")
        elif self.p1 == "Invalid" or self.p2 == "Invalid":
            print("Invalid input. Play again.")


def exchange(inp):
    if inp == 1:
        print("Rock")
        return "rock"
    elif inp == 2:
        print("Paper")
        return "paper"
    elif inp == 3:
        print("Scissors")
        return "scissors"
    else:
        print("Invalid")
        return "Invalid"
        
        
print("Write quit anytime to quit")
x = "none"
y = "none"
while x != "quit" and y != quit:
    x = input("Player1 says : (1 for rock, 2 for paper, 3 for scissors) ")
    if x != "quit":
        i = exchange(int(x))
    else:
        break
    y = input("Player2 says : (1 for rock, 2 for paper, 3 for scissors) ")
    if y != "quit":
        j = exchange(int(y))
    else:
        break
    if i == j:
        print("Tie....")
        continue
    else:
        game = RPS(i, j)
        game.play()


print("Nice Match......")