"""Expense model for the Expense Tracker."""
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Expense:
    amount: float
    category: str
    spent_on: date

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if not self.category.strip():
            raise ValueError("Category is required")