# Generated by Django 4.2.2 on 2023-07-25 22:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0015_remove_registeredcourse_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredexam',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='registeredexam',
            name='paystack_ref',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]