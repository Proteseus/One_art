# Generated by Django 4.0.1 on 2022-02-02 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_alter_artwork_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='status',
        ),
    ]
