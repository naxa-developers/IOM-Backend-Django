# Generated by Django 2.2.6 on 2020-03-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_auto_20200323_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='whymapopenicon',
            name='icon_class',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]