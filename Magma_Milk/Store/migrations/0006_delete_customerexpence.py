# Generated by Django 4.0.2 on 2023-09-08 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_expence_customerexpence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerExpence',
        ),
    ]
