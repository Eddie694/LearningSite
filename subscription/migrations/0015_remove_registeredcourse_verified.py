# Generated by Django 4.2.2 on 2023-07-19 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0014_alter_registeredcourse_paystack_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredcourse',
            name='verified',
        ),
    ]
