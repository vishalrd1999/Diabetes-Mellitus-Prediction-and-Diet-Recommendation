# Generated by Django 3.1.7 on 2021-03-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210306_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activity',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
