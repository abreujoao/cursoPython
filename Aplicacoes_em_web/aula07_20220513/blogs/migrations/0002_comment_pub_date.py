# Generated by Django 4.0.4 on 2022-05-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
