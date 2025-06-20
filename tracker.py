import os
import json
from expense import Expense

class ExpenseTracker:
    def __init__(self,fileName = 'data/expenses.json'):
        self.fileName = fileName
        self.expenses = []
        self.load_expenses()

    def add_expense(self,expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print(f"{'Trasac.No.':<6} | {'Amount':<8} | {'Category':<15} | {'Note':<25} | {'Date':<10}")
        print("-" * 80)

        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i:<6} | ₹{expense.amount:<7.2f} | {expense.category:<15} | {expense.note:<25} | {expense.date:<10}")

    def delete_expense(self,index):
        try:
            removed = self.expenses.pop(index-1)
            print(f"Expense removed: {removed.amount} | {removed.category}")

        except IndexError:
            print("[!] invalid index number. Please view the expenses doc and try again with proper transaction number.")

    def filter_expenses(self,category):
        matches = [e for e in self.expenses if e.category.lower() == category.lower()]
        try:
            if not matches:
                print("None of the Categories matched. please enter a valid category!")
                return
            print(f"{'Trasac.No.':<6} | {'Amount':<8} | {'Category':<15} | {'Note':<25} | {'Date':<10}")
            print("-" * 80)
            for i,expense in enumerate(matches,start = 1):
                print(f"{i:<6} | ₹{expense.amount:<7.2f} | {expense.category:<15} | {expense.note:<25} | {expense.date:<10}")

        except Exception as e:
            print("Error in filtering!")

    def filter_by_month(self,month):
        month = str(month).zfill(2)
        matches = [e for e in self.expenses if e.date.split('-')[1] == month]
        if not matches:
            print("No transaction found from the requested month.")
            return
        print(f"{'Trasac.No.':<6} | {'Amount':<8} | {'Category':<15} | {'Note':<25} | {'Date':<10}")
        print("-" * 80)
        for i,expense in enumerate(matches,start = 1):
            print(f"{i:<6} | ₹{expense.amount:<7.2f} | {expense.category:<15} | {expense.note:<25} | {expense.date:<10}")

    def save_expenses(self):
        try:
            with open(self.fileName,'w') as f:
                data = [expense.to_dict() for expense in self.expenses]
                json.dump(data,f,indent=4)

            print("[✓] Expenses saved successfully.")

        except Exception as e:
            print(f"[!] Error saving expense : {e}")

    def load_expenses(self):
        if not os.path.exists(self.fileName):
            self.expenses = []
            return
        try:
            with open(self.fileName,'r') as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(item) for item in data]

        except json.JSONDecodeError:
            print("[!] Failed to load expenses: Corrupted JSON file?")
            self.expenses = []

        except Exception as e:
            print(f"[!] Error loading the expenses file: {e}")
            self.expenses = []