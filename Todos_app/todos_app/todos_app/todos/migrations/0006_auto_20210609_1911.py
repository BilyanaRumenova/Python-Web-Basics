# Generated by Django 3.2.4 on 2021-06-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_auto_20210609_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home', 'Home stuff'), ('Work', 'Work stuff')], max_length=20),
        ),
    ]
