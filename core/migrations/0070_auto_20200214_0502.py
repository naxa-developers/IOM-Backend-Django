# Generated by Django 2.2.6 on 2020-02-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20200213_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='openspace',
            name='layername',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='openspace',
            name='workspace',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]