from pathlib import Path
from datetime import date
from decimal import Decimal
from django.test import SimpleTestCase

from ..parsers import parse_mt940
from ..data import TransactionDTO

test_dir = Path(__file__).parent


class MT940ParserTest(SimpleTestCase):
    def test_mt940_parser(self):
        mt940 = """
:20:0000000000
:25:NL99ASNB0000000000
:28C:78/1
:60F:C200318EUR10,0
:61:2003180318D10,00NINCNL12RABO0000000000
some name
:86:NL12RABO0000000000 some name

Europese incasso: NL-IDEAL
:62F:C200318EUR0,00
        """
        result = parse_mt940(mt940)
        self.assertEqual(
            len(result), 1, "The transaction list should contain a single transaction"
        )
        self.assertEqual(
            result[0],
            TransactionDTO(
                key=78,
                account="NL99ASNB0000000000",
                other_account="NL12RABO0000000000",
                other_account_name="some name",
                date=date(2020, 3, 18),
                amount=Decimal("-10.00"),
                currency="EUR",
                status="D",
                txtype="NINC",
                remarks="NL12RABO0000000000 some name\nEuropese incasso: NL-IDEAL",
            ),
        )

    def test_mt940_parser_single(self):
        path = Path(test_dir, "fixtures", "single_transaction.940")
        if not path.exists():
            self.skipTest("Fixture with single statement not avaiable.")

        with open(path) as fixture:
            result = parse_mt940(fixture.read())
            self.assertEqual(
                len(result),
                1,
                "The transaction list should contain a single transaction",
            )
            self.assertEqual(result[0].key, 78)
            self.assertEqual(result[0].account, "NL59ASNB0778096270")

    def test_mt940_parser_many(self):
        path = Path(test_dir, "fixtures", "many_transactions.940")
        if not path.exists():
            self.skipTest("Fixture with single statement not avaiable.")

        with open(path) as fixture:
            result = parse_mt940(fixture.read())
            self.assertGreater(
                len(result),
                1,
                "The transaction list should contain more than one transaction",
            )
            self.assertEqual(result[0].key, 78)
            self.assertEqual(result[0].account, "NL59ASNB0778096270")
