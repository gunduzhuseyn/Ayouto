# Generated by Django 2.1.4 on 2018-12-22 18:03

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customermodel_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=users.models.user_profile_image_dir),
        ),
    ]