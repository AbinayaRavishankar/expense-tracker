# 💰 Command-Line Expense Tracker

A minimal, functional, and scalable expense tracker built in **Python** — powered by OOP, file handling, and exception management. Tracks your spending, filters by category/month, and saves your data permanently in a JSON file.

---

## 📦 Features

- ✅ Add new expenses
- ✅ View all recorded expenses in a formatted table
- ✅ Delete an expense by serial number
- ✅ Filter expenses by **category**
- ✅ Filter expenses by **month** (e.g., view all June expenses)
- ✅ Data persists between sessions via JSON file storage
- ✅ Full exception handling for clean, crash-proof execution

---

## 🛠️ Tech Stack

- **Python** (no external libraries)
- JSON for data storage
- Object-Oriented Programming principles
- Modular structure (`Expense` and `ExpenseTracker` classes)

---

## 🧩 Project Structure

```
expenses-tracker/
│
├── main.py              # Entry point with menu and user interaction
├── expense.py           # Expense class (data model)
├── tracker.py           # ExpenseTracker class (logic and file handling)
└── data/
    └── expenses.json    # Your saved expenses live here
```

---

## 🚀 How to Run

```bash
python main.py
```

Follow the on-screen menu to add/view/delete/filter your expenses.

---


## 📘 Notes & Reference (What I Learned)

### 🔁 `json.dump(data, file)`
- Converts a Python list/dictionary into JSON format and **writes it to a file**.
- Used to **save** expenses.
```python
json.dump(data, file, indent=4)
```

### 🔁 `json.load(file)`
- Reads from a `.json` file and **converts it into Python objects** (like a list of dictionaries).
- Used to **load** saved expenses on startup.
```python
data = json.load(file)
```

---

### 🧼 `str.zfill(2)`
- Pads a string with leading zeroes so that it always has a specific length.
- Used to make sure the month (e.g., `6`) becomes `06` so it matches the `"DD-MM-YY"` format.

```python
month = str(6).zfill(2)  # ➡️ "06"
```

---

## 💡 Possible Future Features

- Monthly summary totals
- CSV export
- Category-based analytics
- Terminal color using `colorama`
- GUI (Tkinter or PyQt)
- Budget alerts

---

## 🧠 Author’s Note

> This project was built not just to track expenses — but to **learn** and solidify key Python concepts:
> - OOP
> - Exception handling
> - File I/O
> - Functional design
> - CLI UX

A solid stepping stone toward more complex apps.

---

## 🔗 License

Free to use, fork, and modify for learning purposes. Attribution appreciated!
