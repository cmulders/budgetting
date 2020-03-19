from django.db import models

from .data import TransactionDTO


class Account(models.Model):
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True)


class TransactionManager(models.Manager):
    def create_from_dto(self, dto: TransactionDTO):
        obj, _ = self.get_or_create(
            source=dto.account,
            destination=dto.other_account,
            date=dto.date,
            tx_id=dto.key,
            defaults={
                "currency": dto.currency,
                "amount": dto.amount,
                "status": dto.status,
                "type": dto.txtype,
                "description": dto.remarks,
            },
        )
        return obj


class Transaction(models.Model):
    class Balance(models.TextChoices):
        DEBET = "D"
        CREDIT = "C"

    class TxType(models.Choices):
        INTERNAL = "IOB"

    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=1, choices=Balance.choices)
    date = models.DateField()
    type = models.CharField(max_length=3, choices=TxType.choices)
    tx_id = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    objects = TransactionManager()

    class Meta:
        unique_together = ["source", "destination", "date", "tx_id"]
