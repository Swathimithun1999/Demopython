# Generated by Django 4.2.6 on 2023-10-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-03-22'),
            preserve_default=False,
        ),
    ]
