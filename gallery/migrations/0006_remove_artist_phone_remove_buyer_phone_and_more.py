# Generated by Django 4.0.1 on 2022-02-01 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0005_remove_buyer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='phone',
        ),
        migrations.AddField(
            model_name='artist',
            name='user_type',
            field=models.CharField(default='Artist', max_length=20),
        ),
        migrations.AddField(
            model_name='buyer',
            name='user_type',
            field=models.CharField(default='Buyer', max_length=20),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
