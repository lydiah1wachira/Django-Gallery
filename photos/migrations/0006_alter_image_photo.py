# Generated by Django 4.0.4 on 2022-06-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_location_image_photo_image_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery_images/'),
        ),
    ]
