# Generated by Django 2.2.7 on 2019-11-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20191129_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reported_by',
            field=models.TextField(blank=True, null=True),
        ),
    ]