from datetime import datetime

class Expense:
    def __init__(self, amount, category, note = "", date = None):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date if date else datetime.now().strftime("%d-%m-%Y")

    
    def to_dict(self):
        return {
            'amount' : self.amount,
            'category' : self.category,
            'note' : self.note,
            'date' : self.date
        }
    
    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data['amount'],
            category=data['category'],
            note=data.get('note',''),
            date=data.get('date')
        )