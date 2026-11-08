import pytest
from pathlib import Path
from expenses import ExpenseManager


def test_add_one_expense() -> None:

    manager = ExpenseManager()
    manager.add("Coffee", 12.5)
    assert len(manager.expenses) == 1

def test_add_two_expenses() -> None:
    manager = ExpenseManager()
    manager.add("Coffee", 12.5)
    manager.add("Rent", 4000)
    assert len(manager.expenses) == 2    
def test_save_and_load(tmp_path: Path) -> None:
    file_path = str(tmp_path / "expenses.json")
    manager = ExpenseManager()
    manager.add("Test item", 1.0)
    manager.save(file_path)

    loaded = ExpenseManager()
    loaded.load(file_path)
    assert len(loaded.expenses) == 1
    assert loaded.expenses[0].description == "Test item"
@pytest.mark.parametrize("amount", [0, -0.01, -50])
def test_invalid_amount_rejected(amount: float) -> None:
    manager = ExpenseManager()
    with pytest.raises(ValueError):
        manager.add("Refund", amount)
def test_load_csv_converts_types(tmp_path: Path) -> None:
    csv_file = tmp_path / "expenses.csv"
    csv_file.write_text("description,amount,paid\nRent,4000,True\n")

    manager = ExpenseManager()
    manager.load_csv(str(csv_file))
    expense = manager.expenses[0]

    assert expense.amount == 4000.0
    assert type(expense.amount) == float
    assert expense.paid == True