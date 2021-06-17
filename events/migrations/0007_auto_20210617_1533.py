# Generated by Django 3.2.3 on 2021-06-17 15:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
