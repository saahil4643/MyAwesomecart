# Generated by Django 5.1.2 on 2024-11-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]