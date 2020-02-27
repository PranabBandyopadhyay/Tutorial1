import json
from collections import Counter
birthday = "C:\\Users\\Banerjea-PC\\OneDrive\\Documents\\Python_saved\\birthdays.json"

with open(birthday, 'r') as file:
    dict = json.load(file)
lob = []
month = {
    '1' : 'January',
    '2' : 'February',
    '3' : 'March',
    '4' : 'April',
    '5' : 'May',
    '6' : 'June',
    '7' : 'July',
    '8' : 'August',
    '9' : 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'

}
for bdays in dict.keys():
    day = int(dict[bdays].split("/")[0])
    lob.append(month[str(day)])

a = Counter(lob)
def data():
    if __name__ == "__main__":
        print(a)
    else:
        return(a)