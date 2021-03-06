# Generated by Django 2.1.4 on 2018-12-18 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sold', models.BooleanField(default=False)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('post_name', models.CharField(default='', max_length=150)),
                ('car_price', models.CharField(default='', max_length=100)),
                ('car_brand', models.CharField(default='', max_length=100)),
                ('car_year', models.CharField(default='', max_length=100)),
                ('car_body_type', models.CharField(default='', max_length=100)),
                ('car_mileage', models.CharField(default='', max_length=100)),
                ('car_transmission', models.CharField(default='', max_length=100)),
                ('car_engine_size', models.CharField(default='', max_length=100)),
                ('car_fuel_type', models.CharField(default='', max_length=100)),
                ('car_engine_power', models.CharField(default='', max_length=100)),
                ('car_top_speed', models.CharField(default='', max_length=100)),
                ('car_acceleration', models.CharField(default='', max_length=100)),
                ('car_seats', models.CharField(default='', max_length=100)),
                ('car_doors', models.CharField(default='', max_length=100)),
                ('car_colour', models.CharField(default='', max_length=100)),
                ('car_fuel_consumption', models.CharField(default='', max_length=100)),
                ('car_fuel_capacity', models.CharField(default='', max_length=100)),
                ('post_description', models.TextField(default='', max_length=900)),
                ('post_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
