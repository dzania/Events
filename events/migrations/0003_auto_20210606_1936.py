# Generated by Django 3.2.3 on 2021-06-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210606_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
