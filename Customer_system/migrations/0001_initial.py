# Generated by Django 4.2.3 on 2023-07-10 09:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('password', models.CharField(max_length=6, verbose_name='Password')),
                ('username', models.CharField(max_length=32, verbose_name='User name')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 18, 16, 35))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
