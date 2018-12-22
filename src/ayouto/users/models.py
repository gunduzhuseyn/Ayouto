from django.db import models

from django.contrib.auth.models import User


def user_profile_image_dir(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class ManufacturerVerificationCodeModel(models.Model):
    email = models.EmailField(default='')
    verification_code = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.email


class CustomerModel(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    seller_status = models.IntegerField(default=0)
    # TODO: use a better format to store and validate phone numbers
    # https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    telephone_number = models.CharField(default='', max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to=user_profile_image_dir, blank=True)

    def __str__(self):
        return self.user.username


class ManufacturerModel(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    telephone_number = models.CharField(default='', max_length=50, blank=True, null=True)
    company_name = models.CharField(default='', max_length=100)
    company_address = models.CharField(default='', max_length=300)
    company_number = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.company_name


class UserBankAccount(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

