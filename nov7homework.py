Lod = []
categories = {0, 1}
categories.remove(0)
categories.remove(1)
#This is a group of expenses
def desplaycat():
    for b in Lod:
        categories.add(b['type'])
        print("Categories available:")
    for y in categories:
        print(y)
    categories.remove()
def addexpenses():
    #This adds expenses
    total = 0
    #This calculates the total cost
    while True:
        #Forever
        cost = int(input("How much did it cost?\n$"))
        category = input("What is the category?\n")
        description = input("Description:\n")
        time = input("When did you buy this?\n")
        person = input("Who are you?\n")
        #these find the input of the user
        dictionary = {
            "cost" : cost,
            "type" : category,
            "description" : description,
            "time" : time,
            "person" : person
        }
        #This stores datas with a key
        Lod.append(dictionary)
        #this adds the value to the group
        total = total + cost
        #this finds the total sum of the costs
        print(f"added {cost} to total. \nTotal:{total}")
        #this shows the total
        con = input("continue?(y or n)")
        #this asks if the viewer wants to continue
        if con == "y":
            continue
        else:
            break
def viewallexpenses():
    #This function allows the user to see all expenses
    for i in Lod:
        print(i)
def totalcost():
    #This allows the user to see the total of the expenses
    totalcost = sum(Lod['cost'] for Lod in Lod)
    print(totalcost)
def viewcategory():
    desplaycat()
    wc = input("What category would you like to find?\n")
    if wc == "food":
        for e in Lod:
            if e['type'] == "food":
                print(e)
    elif wc == "entertainment":
        for e in Lod:
            if e['type'] == "entertainment":
                print(e)
    elif wc == "edcuation":
        for e in Lod:        
            if e['type'] == "education":
                print(e)
    elif wc == "technology":    
        for e in Lod:        
            if e['type'] == "technology":
                print(e)
    elif wc == "home":    
        for e in Lod:        
            if e['type'] == "home":
                print(e)
    else:
        print("This category was not found.\nHere are the other purchases:")
        for e in Lod:
            if e['type'] != "food" and e['type'] != "entertainment" and e['type'] != "education" and e['type'] != "technology" and e['type'] != "home":
                print(e)
def removecat():
    #desplays the categories
    desplaycat()
    rc = input("What category would you like to remove?\n")
    for c in Lod:
        if c['type'] == rc:
            Lod.remove(c)
def save(): 
    a = open("savedexpenses.txt", "a")
    for xy in Lod:
        za = f"{"Cost: $"+str(xy['cost'])}, {"Category: " + xy['type']}, {"Description: " + xy['description']}, {"Date: " + xy['time']}, {"User: "+xy['person']}\n"
        a = open("savedexpenses.txt", "r")
        if za in a:
            continue
        else:
            a = open("savedexpenses.txt", "a")
            a.write(za)
    print("expenses were saved in savedexpenses.txt")
def main():
    print("Welcome to CHEE$E\nA multi-millionaire company designed to track your money")
    print("____       ____ ____ __|__ ____")
    print("|    |___| |__  |__  |_|_  |___")
    print("|___ |   | |___ |___  _|_| |___")
    while True:
        choice = int(input("Choose an option:\n1. Add Expense\n2. View all Expenses\n3. Calculate Total Expenses\n4. View Expenses by Category\n5. Save Expenses\n6. Remove Category\n7. Quit\n"))
        #This allows users to choose between which function to use
        if choice == 1: 
            addexpenses()
        elif choice == 2:
            viewallexpenses()
        elif choice == 3:
            totalcost()
        elif choice == 4:
            viewcategory()
        elif choice == 5:
            save()
        elif choice == 6:
            removecat()
        elif choice == 7:
            break
main()

