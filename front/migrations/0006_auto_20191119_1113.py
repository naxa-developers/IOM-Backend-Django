# Generated by Django 2.2.7 on 2019-11-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20191119_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='num1',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num2',
            field=models.CharField(max_length=14),
        ),
    ]
