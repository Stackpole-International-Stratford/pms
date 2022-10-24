# Generated by Django 4.1.2 on 2022-10-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode_verify', '0006_alter_lasermark_scanned_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lasermark',
            old_name='scanned_at',
            new_name='duplicate_scan_at',
        ),
        migrations.AddField(
            model_name='lasermark',
            name='quality_scan_at',
            field=models.DateTimeField(null=True),
        ),
    ]
