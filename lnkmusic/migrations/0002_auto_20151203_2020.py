# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lnkmusic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_slug', models.SlugField()),
                ('show_date', models.DateField()),
                ('attendance', models.IntegerField()),
                ('ticketprice', models.IntegerField()),
                ('grossrevenue', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_slug', models.SlugField()),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Vega',
            new_name='Genre',
        ),
        migrations.DeleteModel(
            name='Bourbon',
        ),
        migrations.DeleteModel(
            name='PBA',
        ),
        migrations.DeleteModel(
            name='SingleBarrel',
        ),
        migrations.AddField(
            model_name='show',
            name='genre',
            field=models.ForeignKey(to='lnkmusic.Genre'),
        ),
        migrations.AddField(
            model_name='show',
            name='venue',
            field=models.ForeignKey(to='lnkmusic.Venue'),
        ),
    ]
