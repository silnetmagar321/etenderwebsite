# Generated by Django 3.0.3 on 2020-07-09 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20200708_1030'),
        ('accounts', '0002_auto_20200707_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='allowed_memberships',
            field=models.ManyToManyField(to='memberships.Membership'),
        ),
    ]
