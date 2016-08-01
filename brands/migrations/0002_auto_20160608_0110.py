# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='user',
        ),
    ]
