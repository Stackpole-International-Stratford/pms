# Generated by Django 4.1.5 on 2023-06-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0019_barcodepun_parts_per_layer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barcodepun',
            name='parts_per_layer',
        ),
        migrations.AddField(
            model_name='barcodepun',
            name='parts_per_tray',
            field=models.IntegerField(default=0),
        ),
    ]
