# Generated by Django 4.2.2 on 2023-07-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0009_alter_registeredcourse_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcourse',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
