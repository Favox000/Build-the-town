# Generated by Django 5.2 on 2025-06-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_profile_room_index_alter_room_user_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='points',
            field=models.IntegerField(default=1, verbose_name='Kolik přidá bodů'),
        ),
    ]
