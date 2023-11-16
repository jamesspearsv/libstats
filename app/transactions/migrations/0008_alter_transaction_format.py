# Generated by Django 4.2 on 2023-04-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='format',
            field=models.CharField(choices=[('in-person', 'In-Person'), ('phone', 'Phone'), ('virtual', 'Virtual')], max_length=64),
        ),
    ]