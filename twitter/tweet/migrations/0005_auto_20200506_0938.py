# Generated by Django 3.0.5 on 2020-05-06 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_auto_20200506_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 9, 38, 13, 375814), verbose_name='現在の時刻'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 9, 38, 13, 374823), verbose_name='現在の時刻'),
        ),
    ]
