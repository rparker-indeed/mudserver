# Generated by Django 3.1 on 2020-08-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]