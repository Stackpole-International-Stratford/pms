# Generated by Django 4.1.2 on 2022-10-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0005_lasermarkmeasurementdata_alter_lasermark_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lasermark',
            name='scanned_at',
            field=models.DateTimeField(null=True),
        ),
    ]