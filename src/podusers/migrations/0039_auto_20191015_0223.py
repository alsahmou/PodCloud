# Generated by Django 2.0.7 on 2019-10-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0038_auto_20191014_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_mp3',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
    ]
