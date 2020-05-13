# Generated by Django 2.2.6 on 2020-04-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0029_auto_20191115_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='administrative_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='gpf.AdministrativeEntity', verbose_name='administrative_entity'),
        ),
    ]