# Generated by Django 3.2 on 2021-05-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='description',
            field=models.TextField(default='', max_length=132),
        ),
    ]
