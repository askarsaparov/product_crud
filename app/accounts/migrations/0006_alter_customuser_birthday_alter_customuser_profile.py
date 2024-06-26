# Generated by Django 5.0.3 on 2024-03-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ImageField(blank=True, default='default/profile_picture/image.png', upload_to='users/', verbose_name='profile'),
        ),
    ]
