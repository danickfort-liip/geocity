# Generated by Django 2.2.6 on 2019-10-22 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0020_auto_20190515_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permitrequest',
            name='archeology_status',
        ),
        migrations.DeleteModel(
            name='ArcheoStatus',
        ),
    ]
