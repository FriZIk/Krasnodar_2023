# Generated by Django 3.2.20 on 2023-07-15 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketorder',
            name='costPlatzcard',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='costService',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='costTicket',
            field=models.FloatField(),
        ),
    ]
