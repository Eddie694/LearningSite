# Generated by Django 4.2.2 on 2023-07-25 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0016_registeredexam_date_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registeredexam',
            options={'ordering': ('-date_created',)},
        ),
    ]
