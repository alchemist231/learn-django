# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_auto_20150619_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_update_time',
            new_name='update_time',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
