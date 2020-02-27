if __name__ == "__main__":

    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

    print("Welcome to the birthday dictionary. We know the birthdays of:")

    for entry in birthdays.keys():
        print(entry)

    done = "N"
    while done != "Y":
        person = input("Who's birthday do you want to look up?")
        if person in birthdays.keys():
            print(str(person) + "'s birthday is " + str(birthdays[person]))
        else:
            print("We dont know him. Is the spelling write ?")
        done = input("Again ? (Y/N)")