# Generated by Django 4.1.1 on 2022-11-30 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="email",
        ),
    ]
