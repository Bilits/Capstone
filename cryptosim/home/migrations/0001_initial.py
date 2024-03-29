# Generated by Django 3.1.6 on 2021-02-26 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='hi', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('postal_code', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=120)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('beginner', models.BooleanField(default=False)),
                ('professional', models.BooleanField(default=False)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, null=True)),
                ('tether', models.FloatField(default=0, null=True)),
                ('bitcoin', models.FloatField(default=0, null=True)),
                ('ethereum', models.FloatField(default=0, null=True)),
                ('ripple', models.FloatField(default=0, null=True)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, null=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.coin')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wallet')),
            ],
        ),
    ]
