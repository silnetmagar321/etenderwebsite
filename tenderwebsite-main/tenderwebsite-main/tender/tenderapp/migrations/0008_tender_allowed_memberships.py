# Generated by Django 3.0.3 on 2020-07-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20200708_1030'),
        ('tenderapp', '0007_auto_20200708_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='allowed_memberships',
            field=models.ManyToManyField(to='memberships.Membership'),
        ),
    ]