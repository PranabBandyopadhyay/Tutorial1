a = [1, 3, 5, 30, 42, 43, 500]

class bin_search:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def binary(self):
        while len(a) > 1:
            c = round(len(a)/2)
            if b > a[c]:
                del a[0:c]
            elif b < a[c]:
                del a[c:len(a)]
            elif b == a[c]:
                print("Match found")
                break
        if len(a) == 1:
            if a[0] == b:
                print("Match found")
            else:
                print("Match not found")

        elif len(a) == 0:
            print("Match not found")


b = int(input("Please input what to search : "))
c = bin_search(a,b)
c.binary()