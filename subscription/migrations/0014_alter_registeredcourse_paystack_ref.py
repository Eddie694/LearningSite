# Generated by Django 4.2.2 on 2023-07-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0013_rename_ref_registeredcourse_paystack_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcourse',
            name='paystack_ref',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
