# Generated by Django 3.0.8 on 2020-07-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogSite', '0006_auto_20200708_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
