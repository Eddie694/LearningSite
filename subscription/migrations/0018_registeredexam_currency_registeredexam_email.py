# Generated by Django 4.2.2 on 2023-07-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0017_alter_registeredexam_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredexam',
            name='currency',
            field=models.CharField(default='NGN', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registeredexam',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
