# Generated by Django 2.2.7 on 2019-11-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_services_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openspace',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
