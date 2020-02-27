import json

birthday = "C:\\Users\\Banerjea-PC\\Documents\\Python_saved\\birthdays.json"

birthdays_dump = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

with open(birthday, 'w') as open_file:
    json.dump(birthdays_dump, open_file)

if __name__ == "__main__":

    done = "Y"
    while done != "N":
        with open(birthday, 'r') as open_file:
            birthdays = json.load(open_file)
        print("Welcome to the birthday dictionary. We know the birthdays of:")

        for entry in birthdays.keys():
            print(entry)
        person = input("Who's birthday do you want to look up?")
        if person in birthdays.keys():
            print(str(person) + "'s birthday is " + str(birthdays[person]))
        else:
            print("We dont know him. Is the spelling write ?")
        nntry = None
        nntry = input("New Entry ? (Y/N)")
        if nntry == "Y":
            name = input("Name ? : ")
            DOB = input("DOB ? (DD/MM/YYYY):")
            birthdays[name] = DOB
            with open(birthday, 'w') as open_file:
                json.dump(birthdays, open_file)
        done = input("Again ? (Y/N)")