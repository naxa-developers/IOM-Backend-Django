# Generated by Django 2.2.7 on 2019-11-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20191129_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openspace',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]