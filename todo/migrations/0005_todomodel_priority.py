# Generated by Django 3.0.8 on 2020-07-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200724_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(default='normal', max_length=50),
            preserve_default=False,
        ),
    ]
