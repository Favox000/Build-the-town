# Generated by Django 5.2 on 2025-06-25 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_codes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codes',
            old_name='add_modey',
            new_name='add_money',
        ),
    ]
