# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 21:47
from __future__ import unicode_literals

import apps.instructor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[apps.instructor.models.validateLengthGreaterThanTwo])),
                ('middle_initial', models.CharField(blank=True, max_length=1)),
                ('last_name', models.CharField(max_length=30, validators=[apps.instructor.models.validateLengthGreaterThanTwo])),
                ('instructor_number', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(max_length=6)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=50, validators=[apps.instructor.models.validateEmail])),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructos', to='login.User')),
            ],
        ),
    ]