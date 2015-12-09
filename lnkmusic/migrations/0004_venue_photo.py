# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lnkmusic', '0003_auto_20151209_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='photo',
            field=models.FileField(null=True, upload_to=b'static/photos', blank=True),
        ),
    ]
