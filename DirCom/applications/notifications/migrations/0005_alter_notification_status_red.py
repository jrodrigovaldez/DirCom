# Generated by Django 4.1.1 on 2022-11-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_notification_status_red'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status_red',
            field=models.CharField(default='UNREAD', max_length=50),
        ),
    ]