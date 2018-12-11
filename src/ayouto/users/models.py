from django.db import models

from django.contrib.auth.models import User


class ManufacturerModel(models.Model):
    representative = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    company_name = models.CharField(default='', max_length=100)
    company_address = models.CharField(default='', max_length=300)
    company_number = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.company_name

