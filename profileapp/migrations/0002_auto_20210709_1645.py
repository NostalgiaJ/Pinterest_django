# Generated by Django 3.2.5 on 2021-07-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='message',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
