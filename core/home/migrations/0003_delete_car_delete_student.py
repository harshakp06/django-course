# Generated by Django 5.0.3 on 2024-04-17 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_car_delete_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]