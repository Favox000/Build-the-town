# Generated by Django 5.2 on 2025-06-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_work_with_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Small_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.PositiveIntegerField(verbose_name='Číslo dne')),
                ('text_question', models.CharField(max_length=250, verbose_name='Text otázky')),
                ('user_answer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Odpověď uživatele')),
            ],
        ),
        migrations.AlterField(
            model_name='work_with_text',
            name='user_answer',
            field=models.TextField(blank=True, null=True, verbose_name='Odpověd uživatele'),
        ),
    ]
