# Generated by Django 3.0.5 on 2020-09-05 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20200905_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model1',
            options={'ordering': ['-pub_date', '-updated', '-timestamp']},
        ),
    ]