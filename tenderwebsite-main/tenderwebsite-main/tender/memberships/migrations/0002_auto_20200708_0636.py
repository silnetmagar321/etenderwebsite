# Generated by Django 3.0.3 on 2020-07-08 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('FiveDays', 'fivedays'), ('Monthly', 'monthly'), ('TwoYears', 'twoyears'), ('FiveYears', 'fiveyears'), ('TenYears', 'tenyears')], default='Free', max_length=30),
        ),
    ]
