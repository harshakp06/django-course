# Generated by Django 5.0.3 on 2024-04-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_description',
            field=models.TextField(default='No Description'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='receipe_name',
            field=models.CharField(max_length=100),
        ),
    ]
