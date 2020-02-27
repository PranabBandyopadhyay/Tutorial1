class ttt:
    def __init__(self, a):
        self.a = a

    def result(self):
        if self.a[0][0] == self.a[0][1] and self.a[0][0] == self.a[0][2]:
            return self.a[0][0]
        elif self.a[0][0] == self.a[1][0] and self.a[0][0] == self.a[2][0]:
            return  self.a[0][0]
        elif self.a[0][1] == self.a[1][1] and self.a[0][1] == self.a[2][1]:
            return self.a[0][1]
        elif self.a[0][2] == self.a[1][2] and self.a[0][2] == self.a[2][2]:
            return self.a[0][2]
        elif self.a[1][0] == self.a[1][1] and self.a[1][0] == self.a[1][2]:
            return self.a[1][0]
        elif self.a[2][0] == self.a[2][1] and self.a[2][0] == self.a[2][2]:
            return self.a[2][0]
        elif self.a[0][0] == self.a[1][1] and self.a[0][0] == self.a[2][2]:
            return self.a[0][0]
        elif self.a[2][0] == self.a[1][1] and self.a[2][0] == self.a[0][2]:
            return self.a[2][0]


winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def play(a):
    t = ttt(a)
    c = t.result()
    if c == 0:
        c = None
    """print("The Player won :-> " + str(c))"""
    return c

play(winner_is_2)
play(winner_is_1)
play(winner_is_also_1)
play(no_winner)
play(also_no_winner)

