# Generated by Django 3.2 on 2021-05-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.URLField()),
                ('description', models.TextField(default='')),
                ('health', models.IntegerField()),
                ('attack', models.IntegerField()),
            ],
        ),
    ]
