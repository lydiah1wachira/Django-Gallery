# Generated by Django 4.0.4 on 2022-05-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_image_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
