# Generated by Django 4.1.1 on 2022-11-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0005_remove_campaigns_date_campaigns_finish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='organized_by',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
