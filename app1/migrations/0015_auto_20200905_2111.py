# Generated by Django 3.0.5 on 2020-09-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20200905_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]