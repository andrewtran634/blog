# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 2, 3, 4, 51, 363000, tzinfo=utc), verbose_name=datetime.datetime(2015, 7, 2, 3, 4, 1, 340000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
