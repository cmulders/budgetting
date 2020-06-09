# Generated by Django 3.0.4 on 2020-03-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('D', 'Debet'), ('C', 'Credit')], max_length=1)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('IOB', 'Internal')], max_length=3)),
                ('tx_id', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'unique_together': {('source', 'destination', 'date', 'tx_id')},
            },
        ),
    ]