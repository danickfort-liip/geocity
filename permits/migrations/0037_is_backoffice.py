# Generated by Django 3.2.4 on 2021-08-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0036_alter_workstype_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permitdepartment',
            name='is_archeologist',
        ),
        migrations.AddField(
            model_name='permitdepartment',
            name='is_backoffice',
            field=models.BooleanField(default=False, help_text='Cocher si les membres font partie du secrétariat. Ils seront notifiés des évolutions de la demande', verbose_name='secrétariat'),
        ),
        migrations.AlterField(
            model_name='permitdepartment',
            name='is_validator',
            field=models.BooleanField(help_text='Cocher si les membres doivent apparaître dans la liste des services consultables pour la validation', verbose_name='validateur'),
        ),
    ]
