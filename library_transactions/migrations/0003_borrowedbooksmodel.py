# Generated by Django 5.0.7 on 2024-08-07 23:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_book', '0001_initial'),
        ('library_transactions', '0002_alter_transactionmodel_transaction_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedBooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='library_book.bookmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
