# Generated by Django 3.0.5 on 2020-04-30 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200430_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='slug',
            field=models.SlugField(default='hello baby'),
        ),
    ]
