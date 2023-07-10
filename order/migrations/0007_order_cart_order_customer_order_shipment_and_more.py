# Generated by Django 4.2.3 on 2023-07-10 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0003_rename_delivery_options_shipment_delivery_method'),
        ('cart', '0005_cart_product'),
        ('Customer_system', '0001_initial'),
        ('order', '0006_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer_system.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ManyToManyField(to='shipment.shipment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now=True),
        ),
    ]
