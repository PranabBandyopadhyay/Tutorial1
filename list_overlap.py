class overlap:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        c = []
        for i in self.a:
            if i in self.b:
                if i not in c:
                    c.append(i)

        return c
