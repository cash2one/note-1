# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('getjson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impapply',
            name='json',
            field=jsonfield.fields.JSONField(default={b'test': 1, b'fields': {b'default': b'', b'type': b'text'}}),
            preserve_default=True,
        ),
    ]
