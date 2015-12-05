# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0002_auto_20151204_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='treatments',
        ),
    ]
