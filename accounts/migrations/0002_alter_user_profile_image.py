# Generated by Django 3.2.13 on 2022-11-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to='image/profile_image'),
        ),
    ]
