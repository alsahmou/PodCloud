# Generated by Django 2.0.7 on 2019-10-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0017_auto_20191010_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poduser',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
