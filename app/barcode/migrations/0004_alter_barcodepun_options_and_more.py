# Generated by Django 4.1.2 on 2022-10-20 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0003_alter_barcodepun_part'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barcodepun',
            options={'ordering': ['part_number']},
        ),
        migrations.RenameField(
            model_name='barcodepun',
            old_name='part',
            new_name='part_number',
        ),
    ]