# Generated by Django 3.1.1 on 2020-10-04 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201004_1820'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]