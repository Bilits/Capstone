# Generated by Django 3.1 on 2021-04-12 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210412_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='price',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='buy',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.AddField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='bitcoin',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='ethereum',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='ripple',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='tether',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.CharField(default='hi', max_length=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.coin'),
        ),
        migrations.DeleteModel(
            name='CoinInWallet',
        ),
    ]
