# Generated by Django 4.0 on 2022-01-01 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bios',
            new_name='bio',
        ),
    ]
