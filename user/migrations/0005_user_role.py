# Generated by Django 4.2.6 on 2023-10-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, default='Not provided', max_length=55),
        ),
    ]
