from expense import Expense
from tracker import ExpenseTracker

tracker = ExpenseTracker()

while True:
    print("\n == Expense Tracker Menu == ")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Filter by category")
    print("5. Filter by month")
    print("6. Save & Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        try:
            amount = float(input("Enter the expense: ₹"))
            category = input("Enter the Category: ")
            note = input("(Optional)What did you spend it for? ")
            expense = Expense(amount,category,note)
            tracker.add_expense(expense)
            print("[✓] Expense Added!")
        except ValueError:
            print("[!] Invalid amount. Please enter a valid number.")


    elif choice == '2':
        tracker.view_expenses()

    elif choice == '3':
        tracker.view_expenses()
        try:
            idx = int(input("Please enter the transaction number you want to delete: "))
            tracker.delete_expense(idx)
        except ValueError:
            print("Please enter a valid transaction number.")

    elif choice == '4':
        try:
            category = input("Enter the category you want to filter:")
            tracker.filter_expenses(category)
        except Exception as e:
            print("Cannot filter: ",e)

    elif choice == '5':
        try:
            month = int(input("Enter the number of the month's expense you want to see (1-Jan/2-Feb/.../12-Dec): "))
            if 1<=month<=12:
                tracker.filter_by_month(month)
            else:
                print("Enter a valid month number.")
        except Exception as e:
            print("[!] something went wrong: ",e)

    elif choice == '6':
        tracker.save_expenses()
        print("Thanks for using this expense tracker. Goodbye!")
        break

    else:
        print("Please enter a valid choice from the menu")