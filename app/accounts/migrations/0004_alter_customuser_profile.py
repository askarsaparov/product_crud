# Generated by Django 5.0.3 on 2024-03-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ImageField(default='default/profile_picture/image.png', upload_to='users/'),
        ),
    ]