# Generated by Django 4.2 on 2023-07-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationplanner',
            name='MoneySpent',
            field=models.IntegerField(default=1),
        ),
    ]
