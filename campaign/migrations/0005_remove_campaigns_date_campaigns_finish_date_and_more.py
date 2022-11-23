# Generated by Django 4.1.1 on 2022-11-23 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_campaigns_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigns',
            name='date',
        ),
        migrations.AddField(
            model_name='campaigns',
            name='finish_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='campaigns',
            name='organized_by',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='campaigns',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
