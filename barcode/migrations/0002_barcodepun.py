# Generated by Django 4.1.2 on 2022-10-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarCodePUN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('part', models.CharField(max_length=10)),
                ('regex', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['part'],
            },
        ),
    ]