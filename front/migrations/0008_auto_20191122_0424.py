# Generated by Django 2.2.7 on 2019-11-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_contact_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openspaceapp',
            name='icon',
            field=models.FileField(upload_to='icon'),
        ),
    ]