# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20160608_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='product',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='sku',
        ),
    ]
