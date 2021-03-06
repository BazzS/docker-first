# Generated by Django 3.0.8 on 2020-07-18 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название события')),
                ('date_start', models.DateTimeField(verbose_name='начало события')),
                ('date_stop', models.DateTimeField(blank=True, verbose_name='конец события')),
                ('reminder', models.DurationField(choices=[(datetime.timedelta(seconds=3600), '1 hour'), (datetime.timedelta(seconds=7200), '2 hours'), (datetime.timedelta(seconds=14400), '4 hours'), (datetime.timedelta(days=1), '1 day'), (datetime.timedelta(days=7), '1 week')], max_length=100, verbose_name='напомнить за')),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'события',
                'db_table': 'my_event',
            },
        ),
    ]
