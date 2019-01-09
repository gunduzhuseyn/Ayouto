from django.contrib import admin

from .models import ManufacturerModel, ManufacturerVerificationCodeModel, CustomerModel

admin.site.register(ManufacturerModel)
admin.site.register(ManufacturerVerificationCodeModel)
admin.site.register(CustomerModel)
