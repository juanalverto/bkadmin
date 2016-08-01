# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=255)),
                ('sku', models.PositiveIntegerField()),
                ('link', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('picture', models.ForeignKey(to='pictures.Picture')),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
    ]
