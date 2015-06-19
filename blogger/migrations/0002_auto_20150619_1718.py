# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_lastname',
            new_name='lastname',
        ),
    ]
