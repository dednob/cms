# Generated by Django 4.1.1 on 2022-10-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_alter_campaigns_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigns',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
