# Generated by Django 3.0.3 on 2020-07-01 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0002_auto_20200627_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tender',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='updated_at',
        ),
    ]
