# Generated by Django 3.1.6 on 2021-04-15 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210414_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sell',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='coin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]