# Generated by Django 3.2.9 on 2022-01-21 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(default=None, max_length=255, null=True)),
                ('stripe_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='payments.stripecustomer')),
            ],
        ),
    ]
