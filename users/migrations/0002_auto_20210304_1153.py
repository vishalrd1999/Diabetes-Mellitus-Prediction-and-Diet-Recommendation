# Generated by Django 3.1.7 on 2021-03-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='alc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bmi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bp',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bpl',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fam',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gen',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='junk',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='med',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phy',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sleep',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='smoking',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sound_sleep',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='stress',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uri',
            field=models.TextField(default=''),
        ),
    ]