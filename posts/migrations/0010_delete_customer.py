# Generated by Django 4.0 on 2021-12-21 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]