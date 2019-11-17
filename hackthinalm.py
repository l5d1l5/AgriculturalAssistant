land = int(input("Hello! Welcome to Agricultural Assistant! This program will help you with all of your farming needs. \n To start, please enter how much land (in square ft) you have: "))
lst = []
print("Currently the crops we support are Grapes, Stawberries, Oranges, Tomatoes, and Almonds")
n = int(input("Enter amount of crops : "))
i = 0
# iterating till the range
while n-1 >= i:
    print("Name of crop: ")
    crops = input()
    crops1 = crops.lower()

    if crops1 == "grapes" or "strawberries" or "oranges" or "tomatoes" or "almonds":
        lst.append(crops1)  # adding the element
        i = i + 1

    elif crops1 != "grapes" or "strawberries" or "oranges" or "tomatoes" or "almonds":
        print("This crop is not supported")

print("We put together some data. Here is some information provided about your crops")
if "grapes" in lst:
    print('''Grape Info: \n Time to Plant: March \n
    Time to harvest: 6 months \n
    Space Taken Up: 36 sq ft \n
    Amount of Water: 8-10 gallons per plant daily \n
    Amount of Pesticide: 2 quarts per 100 square ft twice per year \n
    Sale Price: $2.24 per lb''')
if "strawberries" in lst:
    print('''Strawberries Info: \n Time to Plant: Year round \n
    Time to harvest: 4-6 weeks \n
    Space Taken Up: 21 x 42 in \n
    Amount of Water: 1.5 inch per acre \n
    Amount of Pesticide: 1lb per 20 feet row \n
    Sale Price: $3 per lb''')
if "oranges" in lst:
    print('''Oranges Info: \n Time to Plant: Spring \n
    Time to harvest: 3-4 years \n
    Space Taken Up: 625 sq ft \n
    Amount of Water: 2 inch per acre \n
    Amount of Pesticide: Not recommended \n
    Sale Price: $1.10 per lb''')
if "tomatoes" in lst:
    print('''Tomatoes Info: \n Time to Plant: January \n
    Time to harvest: 8 months \n
    Space Taken Up: 6.25 sq ft \n
    Amount of Water: 1.5 in per acre \n
    Amount of Pesticide: none recommended \n
    Sale Price: $2.01 per lb''')
if "almonds" in lst:
    print('''Almonds Info: \n Time to Plant: Spring \n
    Time to harvest: 5 years \n
    Space Taken Up: 400 sq ft \n
    Amount of Water: 1900 gal per pound of almond \n
    Amount of Pesticide: not recommended \n
    Sale Price: $4 per lb''')

idk = input("Would you like a simplified chard for crop planting. ")
if idk == "yes":
    print('''January: Strawberries, Tomatoes\n 
    February: Strawberries\n
    March: Strawberries, Oranges, Almonds\n
    April: Strawberries, Oranges, Almonds\n
    May: Strawberries, Oranges, Almonds\n
    June: Strawberries\n
    July: Strawberries\n
    August: Strawberries, Almonds\n
    September: Strawberries, Almonds\n
    October: Strawberries, Almonds\n
    November: Strawberries\n
    December: Strawberries\n''')
grapeprice = 2
strawprice = 3
orangeprice = 1
almondprice = 2
tomatoeprice = 4
garea = 36
sarea = 6
oarea = 625
aarea = 6
tarea = 400
if idk == "no":
    print("Ok")
revenue = input("Would you like to know the revenue you will get?")
if revenue == "yes":
    temp = 0
    if "grapes" in lst:
        temp = int(temp)+grapeprice*garea*land
    if "strawberries" in lst:
        temp = int(temp)+strawprice*sarea*land
    if "oranges" in lst:
        temp = int(temp)+orangeprice*oarea*land
    if "almonds" in lst:
        temp = int(temp)+almondprice*aarea*land
    if "tomatoes" in lst:
        temp = int(temp)+tomatoeprice*tarea*land
    print("The amount you will make is")
    print(temp)