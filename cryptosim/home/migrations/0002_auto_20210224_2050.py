# Generated by Django 3.1.6 on 2021-02-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='tether',
            field=models.FloatField(default=0, null=True),
        ),
    ]
