Lod = []
def addexpenses():
    total = 0
    while True:
        cost = int(input("How much did it cost?\n"))
        thing = input("What was it?\n")
        description = input("Description:\n")
        time = input("When did you buy this?\n")
        person = input("Who are you?")
        dictionary = {
            "cost" : cost,
            "type" : thing,
            "description" : description,
            "time" : time,
            "person" : person
        }
        Lod.append(dictionary)
        total = total + cost
        print(f"added {cost} to total. \nTotal:{total}")
        con = input("continue?(y or n)")
        if con == "y":
            continue
        else:
            break
def viewallexpenses():
    for i in Lod:
        print(i)
def totalcost():
    totalcost = sum(Lod['cost'] for Lod in Lod)
    print(totalcost)
while True:
    choice = int(input("Choose an option:\n1. Add Expense\n2. View all Expenses\n3. Calculate Total Expenses\n4. View Expenses by Category\n5. Save Expenses\n6. Quit"))
    if choice == 1: 
        addexpenses()
    elif choice == 2:
        viewallexpenses()
    elif choice == 3:
        totalcost()
    elif choice == 4:
        continue
    elif choice == 5:
        continue
    elif choice == 6:
        break

