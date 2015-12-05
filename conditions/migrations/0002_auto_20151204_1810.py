# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('treatment', models.CharField(help_text=b'name of treatment', max_length=256)),
                ('description', models.CharField(help_text=b'description of treatment', max_length=500)),
                ('display_name', models.CharField(help_text=b'brief name of treatment for display', max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='condition',
            name='treatments',
            field=models.CharField(default=b'treatments not yet known', help_text=b'treatments for condition', max_length=256),
        ),
        migrations.AddField(
            model_name='treatment',
            name='condition',
            field=models.ForeignKey(to='conditions.Condition'),
        ),
    ]
