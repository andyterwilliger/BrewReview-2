# Generated by Django 4.0.2 on 2022-02-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_beer_abv_beer_location_beer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
