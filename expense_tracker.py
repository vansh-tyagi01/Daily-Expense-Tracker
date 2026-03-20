print("*..........DAILY EXPENSE TRACKER..........*")
print(" ")

expense = []


# add expense

def add_expense():
    name = input("Enter your name:")
    exp = input("Enter name of expense Today:")
    price = int(input("Enter expense price:"))

    expense.append([name,exp,price])



# show expense

def show_expense():
    if len(expense)==0:
        print("Empty expense record...")
    else:
        print("Expense Record :",expense)



# calculate price

def calculate_price():
    total = 0
    for record in expense:
        total+=record[2]
    print("Total Price :",total)



# delete expense

def delete_expense():
    name = input("Enter your name to delete expense:")
    exp = input("Enter your expense name to delete:")
    price = int(input("Enter expense price:"))
    
    found = False

    for r in expense:
        if name == r[0] and exp == r[1]:

            found = True

            if price > r[2]:
                print("your price quantity greater than stored price , this is not Available")
            elif price == r[2]:
                expense.remove(r)
                print(f"{name} your expense {exp} is delete successfully👍")
            else:
                print(f"{price} is delete successfully in {r[2]}")
                r[2]-=price
                print("Remaining Price :",r[2])
    if not found:
        print(f"{name} and {exp} record is not Exist")
            
            

while True:
    print(" ")
    print(" ")
    print("1. Add Expense\n2. Show Expense\n3. Show Price of Expense\n4. Delete Expense\n5. Exit")
    ch=int(input("Enter your choice?:"))
    if ch == 1:
        add_expense()
    elif ch == 2:
        show_expense()
    elif ch == 3:
        calculate_price()
    elif ch == 4:
        delete_expense()
    elif ch == 5:
        print("*...Program Exit...*")
        break