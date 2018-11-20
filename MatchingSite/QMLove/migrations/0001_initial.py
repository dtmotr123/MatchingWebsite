# Generated by Django 2.1 on 2018-11-20 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby_name', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Skiing'), ('2', 'Fishing'), ('3', 'Hunting'), ('4', 'Golf'), ('5', 'Reading'), ('6', 'Football'), ('7', 'Automobiles'), ('8', 'Fitness'), ('9', 'Politics'), ('10', 'Fashion'), ('11', 'Art')], max_length=23, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('dob', models.DateField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hobby',
            name='users',
            field=models.ManyToManyField(to='QMLove.Profile'),
        ),
    ]
