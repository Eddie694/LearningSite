# Generated by Django 4.2.2 on 2023-07-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acetelapp', '0003_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]