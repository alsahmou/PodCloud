# Generated by Django 2.0.7 on 2019-11-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0006_auto_20191111_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_image',
            field=models.ImageField(blank=True, default='alisahmoud.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='poduser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='alisahmoud.jpg', null=True, upload_to=''),
        ),
    ]
