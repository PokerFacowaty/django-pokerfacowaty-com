# Generated by Django 4.2 on 2023-08-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pamlpage',
            name='GAME',
            field=models.BooleanField(default=False),
        ),
    ]