# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_auto_20160608_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='Name',
            new_name='brand_name',
        ),
    ]
