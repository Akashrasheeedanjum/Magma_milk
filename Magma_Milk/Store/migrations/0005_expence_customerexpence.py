# Generated by Django 4.0.2 on 2023-09-08 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_stor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expence_name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerExpence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expence_type', models.TextField(blank=True, null=True)),
                ('expence_amount', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.customer')),
            ],
        ),
    ]
