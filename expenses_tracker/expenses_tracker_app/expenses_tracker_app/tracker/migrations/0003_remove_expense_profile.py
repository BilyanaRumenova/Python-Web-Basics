# Generated by Django 3.2.4 on 2021-06-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_expense_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='profile',
        ),
    ]
