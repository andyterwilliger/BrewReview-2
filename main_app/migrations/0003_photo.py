# Generated by Django 4.0.2 on 2022-02-21 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_beer_brewery_beer_name_beer_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.beer')),
            ],
        ),
    ]