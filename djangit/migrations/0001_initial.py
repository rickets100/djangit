# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aroma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aroma_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hop_name', models.CharField(max_length=50)),
                ('alpha_acid_low', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('alpha_acid_high', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('beta_acid_low', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('beta_acid_high', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('total_oil_low', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('total_oil_high', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('cohumulone_low', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
                ('cohumulone_high', models.DecimalField(decimal_places=1, default=b'0', max_digits=4)),
            ],
        ),
    ]