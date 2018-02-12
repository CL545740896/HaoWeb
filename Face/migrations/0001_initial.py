# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gongjijing_type', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('job_address', models.CharField(default='\u65e0', max_length=100)),
                ('job_age', models.CharField(default=b'0', max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('shebaotime', models.CharField(default=b'0', max_length=100)),
                ('shebao_type', models.CharField(max_length=100)),
                ('gongjijintime', models.CharField(default=b'0', max_length=100)),
                ('home_address', models.CharField(max_length=100)),
                ('zhimafen', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('result', models.CharField(max_length=100)),
                ('money', models.CharField(max_length=100)),
            ],
        ),
    ]
