# Generated by Django 3.2.13 on 2022-06-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]