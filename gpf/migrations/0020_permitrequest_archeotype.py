# Generated by Django 2.2.6 on 2019-10-22 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0019_archeotype'),
    ]

    operations = [
        migrations.AddField(
            model_name='permitrequest',
            name='archeotype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gpf.ArcheoType', verbose_name='archeo_type'),
        ),
    ]