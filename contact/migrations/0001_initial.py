# Generated by Django 4.1.1 on 2022-10-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.TextField()),
                ('sub', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
    ]
