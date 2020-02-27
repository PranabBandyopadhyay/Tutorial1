i=1
shop_list = []
while (i<=5):
    var = input("Please enter " + str(i) + "th thing name : ")
    shop_list.append(var)
    i = i+1


print("Please find your list of items")
for j in shop_list:
    print(j)

print("print add up your prices : ")
price=0
for k in shop_list:
    price=price+(float(input("price of " + k + ":"))*float(input("how many " + k + ":")))

print("Total Price of all items: " + str(price))
