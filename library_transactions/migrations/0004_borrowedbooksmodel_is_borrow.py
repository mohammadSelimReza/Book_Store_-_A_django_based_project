# Generated by Django 5.0.7 on 2024-08-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_transactions', '0003_borrowedbooksmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbooksmodel',
            name='is_borrow',
            field=models.BooleanField(default=True),
        ),
    ]
