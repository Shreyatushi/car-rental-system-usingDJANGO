# Generated by Django 3.2.13 on 2022-06-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220626_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_no',
            field=models.CharField(default='4F3AE', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
