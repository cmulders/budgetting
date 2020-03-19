from datetime import date
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class TransactionDTO:
    key: int
    account: str
    other_account: str
    other_account_name: str
    date: date
    amount: Decimal
    currency: str
    status: chr
    txtype: str

    remarks: str
