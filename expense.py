from datetime import datetime , timedelta

expense = []

def add_expense():
    title = input("Enter your expense title(eg. phone,car...):")
    category = input("Enter your expense category(eg. food,vehicles...):")
    price = int(input("Enter expense price?:"))
    date = input("Enter date(YYYY-MM-DD)?:")

    expense.append([title , category , price , date])


def delete_expense():
    title = input("Enter your expense title:")
    date = input("Enter correct date(YYYY-MM-DD)?:")
    found = False

    for exp in expense[:]:
        if title == exp[0] and date == exp[3]:
            expense.remove(exp)
            found = True
    if found:
        print("Delete Successfull👍")
    else:
        print("Expense not found✖️")


def show_expense_list():
    if len(expense)==0:
        print("No Record Found⏺️")
    else:
        print("Expense :",expense)


def weekly_expense():
    total = 0
    today = datetime.today()

    seven_days_ago = today - timedelta(days=7)

    for exp in expense:
        exp_date = datetime.strptime(exp[3], "%Y-%m-%d")

        if exp_date>=seven_days_ago:
            total+=exp[2]
        
    print("Weekly Expense :", total)



def monthly_expense():
    total = 0
    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)

    for exp in expense:
        exp_date = datetime.strptime(exp[3],"%Y-%m-%d")

        if exp_date >= thirty_days_ago:
            total+=exp[2]
    
    print("Monthely Expense :",total)


def year_expense():
    total = 0
    today = datetime.today()
    one_year_ago = today - timedelta(days=365)

    for exp in expense:
        exp_date = datetime.strptime(exp[3],"%Y-%m-%d")
        if exp_date >= one_year_ago:
            total+=exp[2]
    
    print("Year Expense :",total)


while True:
    print("1. Add Expense\n2. Delete Expense\n3. Show Expense\n4. See Weekly Expense\n5. See Monthly Expense\n6. Year Expense\n7. Exit\n")

    ch = int(input("Enter your choice?:"))
    if ch == 1:
        add_expense()
    elif ch == 2:
        delete_expense()
    elif ch == 3:
        show_expense_list()
    elif ch == 4:
        weekly_expense()
    elif ch == 5:
        monthly_expense()
    elif ch == 6:
        year_expense()
    elif ch == 7:
        print("*....Exit Program....*")
        break






