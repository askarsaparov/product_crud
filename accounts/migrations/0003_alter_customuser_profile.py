# Generated by Django 5.0.3 on 2024-03-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ImageField(blank=True, default='default/profile_picture/image.png', null=True, upload_to='users/'),
        ),
    ]
