# Generated by Django 4.1.3 on 2023-01-15 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0011_lasermarkduplicatescan_lasermarkqualityscan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lasermark',
            name='duplicate_scan_at',
        ),
        migrations.RemoveField(
            model_name='lasermark',
            name='quality_scan_at',
        ),
    ]
