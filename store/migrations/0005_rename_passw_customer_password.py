# Generated by Django 3.2.5 on 2021-09-19 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='passw',
            new_name='password',
        ),
    ]
