# Generated by Django 4.2.6 on 2023-11-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_employees_images_employees_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]