# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lnkmusic', '0002_auto_20151203_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='ticketprice',
            field=models.FloatField(),
        ),
    ]
