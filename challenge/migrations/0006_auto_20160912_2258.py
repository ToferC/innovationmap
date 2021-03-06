# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-13 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_auto_20160912_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField(max_length=255)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='project',
            name='teams',
        ),
        migrations.AlterField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(blank=True, to='challenge.Tag'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tags',
            field=models.ManyToManyField(blank=True, to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='committment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Project'),
        ),
        migrations.AddField(
            model_name='committment',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Team'),
        ),
    ]
