# Generated by Django 4.2.4 on 2023-11-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_drink_alter_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='drink',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]