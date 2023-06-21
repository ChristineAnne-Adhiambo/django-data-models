# Generated by Django 4.2.1 on 2023-06-19 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_payment_options_payment_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='receipt_number',
            field=models.CharField(max_length=32),
        ),
    ]
