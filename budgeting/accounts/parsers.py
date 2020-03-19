from datetime import date
import mt940

from .data import TransactionDTO


def make_dto(transaction):
    tx_data = transaction.data
    account_data = transaction.transactions.data
    return TransactionDTO(
        amount=tx_data["amount"].amount,
        currency=tx_data["amount"].currency,
        account=account_data["account_identification"],
        other_account=tx_data["customer_reference"],
        date=date(tx_data["date"].year, tx_data["date"].month, tx_data["date"].day),
        other_account_name=tx_data["extra_details"],
        remarks=tx_data["transaction_details"],
        status=tx_data["status"],
        txtype=tx_data["id"],
        key=int(account_data["statement_number"]),
    )


def parse_mt940(stream):
    tag_parser = mt940.tags.StatementASNB()

    transactions = mt940.models.Transactions(
        processors={
            "pre_statement": [mt940.processors.add_currency_pre_processor("EUR")]
        },
        tags={tag_parser.id: tag_parser},
    )

    transactions.parse(stream)
    return [make_dto(tx) for tx in transactions]
