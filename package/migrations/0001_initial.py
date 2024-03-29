# Generated by Django 2.2.2 on 2019-07-29 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('starting_point', models.CharField(max_length=200)),
                ('ending_point', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('details', models.TextField()),
                ('type_of_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.TripType')),
            ],
        ),
    ]
