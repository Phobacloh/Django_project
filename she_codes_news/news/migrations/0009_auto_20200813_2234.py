# Generated by Django 3.0.8 on 2020-08-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200812_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
