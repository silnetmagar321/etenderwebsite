# Generated by Django 3.0.3 on 2020-07-08 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0006_remove_pricingclientinfo_any_other_supply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='last_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
