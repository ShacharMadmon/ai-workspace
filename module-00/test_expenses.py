import pytest
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
def test_negative_amount_rejected() -> None:
    manager = ExpenseManager()
    with pytest.raises(ValueError):
        manager.add("Refund", -50)