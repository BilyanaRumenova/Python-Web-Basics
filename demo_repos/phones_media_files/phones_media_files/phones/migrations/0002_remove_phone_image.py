# Generated by Django 3.2.5 on 2021-07-08 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='image',
        ),
    ]
