# Generated by Django 2.2.6 on 2019-10-25 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipality', to='core.District')),
            ],
        ),
        migrations.CreateModel(
            name='OpenSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('capacity', models.BigIntegerField(blank=True, null=True)),
                ('total_area', models.IntegerField(blank=True, null=True)),
                ('usable_area', models.IntegerField(blank=True, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='open_space', to='core.District')),
                ('municipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='open_space', to='core.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('open_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_use', to='core.OpenSpace')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('open_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='core.OpenSpace')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('urgency', models.IntegerField(choices=[(0, 'High'), (1, 'Medium'), (2, 'Low')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default=0)),
                ('open_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='core.OpenSpace')),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='openspace',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='open_space', to='core.Province'),
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='core.Province'),
        ),
    ]