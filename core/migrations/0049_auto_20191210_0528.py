# Generated by Django 2.2.7 on 2019-12-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20191205_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationfacility',
            name='amenity',
        ),
        migrations.RemoveField(
            model_name='healthfacility',
            name='amenity',
        ),
        migrations.RemoveField(
            model_name='nearbyamenities',
            name='open_space',
        ),
        migrations.DeleteModel(
            name='ProvinceDummy',
        ),
        migrations.AlterField(
            model_name='openspace',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='openspace',
            name='catchment_area',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='openspace',
            name='issue',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='openspace',
            name='ownership',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='EducationFacility',
        ),
        migrations.DeleteModel(
            name='HealthFacility',
        ),
        migrations.DeleteModel(
            name='NearbyAmenities',
        ),
    ]
