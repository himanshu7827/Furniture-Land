# Generated by Django 3.2.3 on 2021-12-23 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
