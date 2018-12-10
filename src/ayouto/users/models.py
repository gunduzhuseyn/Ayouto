from django.db import models

from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.user.username

