# Generated by Django 3.0.8 on 2020-08-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200812_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]