# Generated by Django 3.1 on 2020-09-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20200822_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='exit_down',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='exit_up',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
