# Generated by Django 3.2.9 on 2022-01-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cows', '0002_cow_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='description',
            field=models.TextField(default='', max_length=10000),
        ),
    ]
