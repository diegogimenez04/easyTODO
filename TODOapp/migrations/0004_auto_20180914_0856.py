# Generated by Django 2.0.4 on 2018-09-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOapp', '0003_auto_20180907_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='archive',
            field=models.BooleanField(default=True),
        ),
    ]