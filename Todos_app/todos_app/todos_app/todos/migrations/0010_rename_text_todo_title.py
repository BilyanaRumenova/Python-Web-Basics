# Generated by Django 3.2.4 on 2021-06-21 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_auto_20210610_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='title',
        ),
    ]
