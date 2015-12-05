# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0003_remove_condition_treatments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatment',
            old_name='treatment',
            new_name='treatment_name',
        ),
    ]
