# Generated by Django 5.1.2 on 2024-11-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email_id',
            new_name='email',
        ),
    ]