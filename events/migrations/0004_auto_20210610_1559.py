# Generated by Django 3.2.3 on 2021-06-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210606_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
