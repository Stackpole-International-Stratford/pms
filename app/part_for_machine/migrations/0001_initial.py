# Generated by Django 4.2.2 on 2023-08-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartForMachineEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('part', models.CharField(max_length=30)),
                ('line', models.CharField(max_length=30)),
                ('asset', models.CharField(max_length=10)),
            ],
        ),
    ]
