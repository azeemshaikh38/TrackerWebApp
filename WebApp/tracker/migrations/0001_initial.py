# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 02:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='ActivityFieldEffects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.FloatField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Activities')),
            ],
            options={
                'db_table': 'ActivityFieldEffects',
            },
        ),
        migrations.CreateModel(
            name='ActivitySubfieldEffects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.FloatField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Activities')),
            ],
            options={
                'db_table': 'ActivitySubfieldEffects',
            },
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='Subfields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Fields')),
            ],
            options={
                'db_table': 'Subfields',
            },
        ),
        migrations.CreateModel(
            name='UserActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Activities')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserActivities',
            },
        ),
        migrations.CreateModel(
            name='UserFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Fields')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserFields',
            },
        ),
        migrations.CreateModel(
            name='UserSubfields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('subfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Subfields')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserSubfields',
            },
        ),
        migrations.AddField(
            model_name='activitysubfieldeffects',
            name='subfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Subfields'),
        ),
        migrations.AddField(
            model_name='activityfieldeffects',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Fields'),
        ),
    ]
