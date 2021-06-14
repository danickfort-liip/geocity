# Generated by Django 3.2.4 on 2021-06-10 07:32

from django.db import migrations
from permits import admin


def set_default_integrator_on_existing_objects(apps, schema_editor):

    # Get the reference to required models without importing them
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    Department = apps.get_model('permits', 'PermitDepartment')
    PermitAdministrativeEntity = apps.get_model('permits', 'PermitAdministrativeEntity')
    PermitActorType = apps.get_model('permits', 'PermitActorType')
    WorksType = apps.get_model('permits', 'WorksType')
    WorksObjectType = apps.get_model('permits', 'WorksObjectType')
    WorksObject = apps.get_model('permits', 'WorksObject')
    WorksObjectProperty = apps.get_model('permits', 'WorksObjectProperty')
    PermitRequestAmendProperty = apps.get_model('permits', 'PermitRequestAmendProperty')

    # Create default group and departement associated with it
    already_applied_migration = Group.objects.filter(
        name='default_integrator'
    ).exists()

    if already_applied_migration:
        self.stdout.write('This data migration has already been applied. Not applying')
        return

    integrator_group = Group.objects.create(
        name='default_integrator'
    )

    integrator_departement = Department.objects.create(
        description='default_integrator',
        is_default_validator = False,
        is_validator = False,
        is_integrator_admin = True,
        is_archeologist = False,
        group = integrator_group
    )

    # Update models to set default integrator
    PermitAdministrativeEntity.objects.update(integrator=integrator_group)
    PermitActorType.objects.update(integrator=integrator_group)
    WorksType.objects.update(integrator=integrator_group)
    WorksObjectType.objects.update(integrator=integrator_group)
    WorksObject.objects.update(integrator=integrator_group)
    WorksObjectProperty.objects.update(integrator=integrator_group)
    PermitRequestAmendProperty.objects.update(integrator=integrator_group)

    permits_permissions = Permission.objects.filter(
            content_type__app_label="permits",
            content_type__model__in=admin.INTEGRATOR_PERMITS_MODELS_PERMISSIONS,
        )

    other_permissions = Permission.objects.filter(
        codename__in=admin.OTHER_PERMISSIONS_CODENAMES
    )
    
    integrator_group.permissions.set(
            permits_permissions.union(other_permissions)
    )



class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0023_qgis_template_jsonfield_model'),
    ]

    operations = [
        migrations.RunPython(set_default_integrator_on_existing_objects),
    ]
