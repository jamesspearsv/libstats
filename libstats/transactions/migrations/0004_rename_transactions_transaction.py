# Generated by Django 4.2 on 2023-04-16 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transactions_format_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]