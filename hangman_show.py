class hmshow():
    def __init__(self, word, letter, guessed):
        self.word = word
        self.letter = letter.upper()
        self.guessed = guessed

    def show(self):
        _word = []
        length = len(self.guessed)
        if self.letter not in self.word:
            print("Incorrect !!!")
        for l,x in zip(self.word, range(0,length)):
            if self.letter == l:
                _word.append(l)
            elif self.guessed[x] != "_":
                _word.append(self.guessed[x])
            else:
                _word.append("_")
        if __name__ == "__main__":
            print(' '.join(_word))
        else:
            return _word

