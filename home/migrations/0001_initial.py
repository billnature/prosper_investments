# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 14:45
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name=b'Monthly Pay.')),
            ],
            options={
                'default_permissions': ('modify',),
            },
        ),
    ]