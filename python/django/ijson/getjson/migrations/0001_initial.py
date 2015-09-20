# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('json', jsonfield.fields.JSONField(default={b'test': 1})),
                ('state', models.BooleanField(default=False, verbose_name='\u5b9e\u65bd\u5b8c\u6210')),
                ('notes', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': '\u5b9e\u65bd\u7533\u8bf7',
                'verbose_name_plural': '\u5b9e\u65bd\u7533\u8bf7\u5217\u8868',
            },
            bases=(models.Model,),
        ),
    ]
