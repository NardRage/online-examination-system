# Generated by Django 3.2.3 on 2021-06-20 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_question_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=3600)),
        ),
    ]
