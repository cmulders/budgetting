from django.test import TestCase

from ..models import Transaction
from .factories import TransactionDTOFactory


class TransactionTest(TestCase):
    def test_can_create_from_dto(self):
        dto = TransactionDTOFactory.build()
        instance = Transaction.objects.create_from_dto(dto)
        self.assertIsInstance(instance, Transaction)
        self.assertEqual(dto.key, instance.tx_id)
