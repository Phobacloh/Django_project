# Generated by Django 3.0.8 on 2020-08-11 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200810_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='created_date',
        ),
    ]
