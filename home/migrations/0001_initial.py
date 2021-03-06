# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 17:59
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Start date')),
                ('monthly_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name=b'Monthly Pay.')),
            ],
            options={
                'default_permissions': ('modify',),
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date')),
                ('particulars', models.CharField(max_length=255)),
                ('invested', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name=b'Invested.')),
                ('recouped', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name=b'Recouped.')),
                ('interest', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name=b'Interest.')),
            ],
            options={
                'default_permissions': ('modify',),
            },
        ),
    ]
