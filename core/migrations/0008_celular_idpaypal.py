# Generated by Django 2.2 on 2019-05-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190522_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='celular',
            name='idpaypal',
            field=models.CharField(default='', max_length=20),
        ),
    ]
