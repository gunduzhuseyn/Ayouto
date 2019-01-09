from django.db import models

from django.contrib.auth.models import User


class CarPostModel(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    post_time = models.DateTimeField(auto_now_add=True)
    post_name = models.CharField(max_length=150, default='')
    car_price = models.CharField(max_length=100, default='')
    car_brand = models.CharField(max_length=100, default='')
    car_year = models.CharField(max_length=100, default='')
    car_body_type = models.CharField(max_length=100, default='')
    car_mileage = models.CharField(max_length=100, default='')
    car_transmission = models.CharField(max_length=100, default='')
    car_engine_size = models.CharField(max_length=100, default='')
    car_fuel_type = models.CharField(max_length=100, default='')
    car_engine_power = models.CharField(max_length=100, default='')
    car_top_speed = models.CharField(max_length=100, default='')
    car_acceleration = models.CharField(max_length=100, default='')
    car_seats = models.CharField(max_length=100, default='')
    car_doors = models.CharField(max_length=100, default='')
    car_colour = models.CharField(max_length=100, default='')
    car_fuel_consumption = models.CharField(max_length=100, default='')
    car_fuel_capacity = models.CharField(max_length=100, default='')
    post_description = models.TextField(max_length=900, default='')

    def __str__(self):
        return self.post_name

