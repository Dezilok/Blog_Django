# Generated by Django 3.1 on 2020-08-10 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200810_0424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]
