# Generated by Django 5.2 on 2025-06-01 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
    ]
