# Generated by Django 2.0.7 on 2019-11-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0005_auto_20191111_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='podcast_image',
            field=models.ImageField(blank=True, default='url("alisahmoud.jpg")', null=True, upload_to=''),
        ),
    ]
