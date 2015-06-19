# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_text', models.CharField(max_length=400)),
                ('post_update_time', models.DateTimeField(verbose_name=b'date updated')),
                ('upvote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_firstname', models.CharField(max_length=50)),
                ('user_lastname', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_post',
            field=models.ForeignKey(to='blogger.user'),
        ),
    ]
