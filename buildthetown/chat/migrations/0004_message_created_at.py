# Generated by Django 4.2.22 on 2025-06-20 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_sendet_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 20, 17, 54, 42, 703000, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
