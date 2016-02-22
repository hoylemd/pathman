# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 03:00
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('races', '0001_initial'),
        ('classes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(
                    editable=False,
                    populate_from=b'name',
                    unique=True)),
                ('hp', models.IntegerField()),
                ('strength', models.IntegerField(default=10)),
                ('dexterity', models.IntegerField(default=10)),
                ('constitution', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('wisdom', models.IntegerField(default=10)),
                ('charisma', models.IntegerField(default=10)),
                ('race', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='races.Race')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassLevel',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified')),
                ('level', models.IntegerField(default=1)),
                ('character', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='characters.Character')),
                ('the_class', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='classes.Class')),
            ],
            options={
                'abstract': False,
            },
        )
    ]
