# Generated by Django 4.2.6 on 2023-10-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='group',
            field=models.TextField(default='Not provided'),
        ),
    ]
