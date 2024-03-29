# Generated by Django 4.0 on 2021-12-28 16:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.UUID('0e3251cf-73f8-4926-8253-addee34a7d5b'), editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
