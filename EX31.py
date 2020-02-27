from EX30 import guess_a_word
from hangman_show import hmshow
from hangman import hmdraw ## need to improve

word = guess_a_word()
"""print("Guessed word : " + word)"""
length = len(word)
guessed = length*[*"_"]
player_guessed = []
inc_counter = 0
while "_" in guessed:
    l = input("Guess a letter : ").upper()
    if l in player_guessed:
        print("This is your return attempt for letter " + str(l))
    if l not in word:
        player_guessed.append(l)
        inc_counter +=1
        print(inc_counter)
        hmdraw(inc_counter) # need to improve
    if inc_counter == 6:
        print("You missed it. 6 wrong guesses.")
        break
    w = hmshow(word, l, guessed)
    guessed = w.show()
    print(' '.join(guessed))

print("Word was : " + word)