# Generated by Django 2.0.7 on 2019-10-10 06:11

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0016_auto_20191010_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poduser',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31, null=True),
        ),
    ]
