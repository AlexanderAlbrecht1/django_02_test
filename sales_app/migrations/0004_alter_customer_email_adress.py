# Generated by Django 5.2.3 on 2025-06-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0003_customer_account_customer_email_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_adress',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
