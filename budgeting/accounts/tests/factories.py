import factory

from ..data import TransactionDTO


class TransactionDTOFactory(factory.Factory):
    class Meta:
        model = TransactionDTO

    key = factory.Faker('pyint', min_value=0, max_value=366)
    account = factory.Faker('iban')
    other_account = factory.Faker('iban')
    other_account_name = factory.Faker('bs')
    date = factory.Faker('date_between', start_date='-1y', end_date='today')
    amount = factory.Faker('pydecimal', min_value=-200, max_value=200)
    currency = factory.Faker('currency_code')
    status = factory.Faker('random_element', elements=('C', 'D'))
    txtype = factory.Faker('random_element', elements=('NIOB',))
    remarks = factory.Faker('sentences', nb=3, ext_word_list=None)
