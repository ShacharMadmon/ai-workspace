import json
import csv
from pathlib import Path
from dataclasses import dataclass, asdict


@dataclass(slots=True)
class Expense:
    description: str
    amount: float
    paid: bool = False

class ExpenseManager:
    def __init__(self) -> None:
       self.expenses = []

    def add(self, description: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.expenses.append(Expense(description,amount))
    def save(self, path: str) -> None:
        data = []
        for expense in self.expenses:
            data.append(asdict(expense))
        text = json.dumps(data, indent=4)
        Path(path).write_text(text)
    def load(self, path: str) -> None:
        text = Path(path).read_text()
        data = json.loads(text)
        self.expenses = []
        for item in data:
            self.expenses.append(Expense(item["description"], item["amount"], item["paid"]))
    def load_csv(self, path: str) -> None:
        text = Path(path).read_text()
        lines = text.splitlines()
        reader = csv.DictReader(lines)
        self.expenses = []
        for record in reader:
            self.expenses.append(Expense(record["description"], float(record["amount"]), record["paid"] == "True"))

def main() -> None:
    manager = ExpenseManager()
    manager.add("Coffee", 12.5)
    manager.add("Rent", 4000)
    print(manager.expenses)
    try:
        manager.add("Refund", -50)
    except ValueError as e:
        print(e)
    manager.save("module-00/expenses.json")
    loaded = ExpenseManager()
    loaded.load("module-00/expenses.json")
    print("Loaded:", loaded.expenses)
    manager.load("module-00/expenses.json")
    print("Reload:", manager.expenses)
    from_csv = ExpenseManager()
    from_csv.load_csv("module-00/expenses.csv")
    print("From CSV:", from_csv.expenses)


if __name__ == "__main__":
    main()