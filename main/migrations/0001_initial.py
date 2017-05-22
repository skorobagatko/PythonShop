# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('alias', models.SlugField(verbose_name='Alias категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('image', models.CharField(max_length=255, verbose_name='Ссылка на картинку')),
                ('alias', models.SlugField(verbose_name='Alias товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
