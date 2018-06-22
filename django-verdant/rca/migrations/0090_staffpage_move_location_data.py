# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-06 21:26
from __future__ import unicode_literals
import json

from django.db import migrations


def move_location_data(apps, schema_editor):
    """
    Move StaffPage.location to StaffPageRole.location if the user is
    technical.
    """
    StaffPage = apps.get_model('rca', 'StaffPage')

    # Move location data to roles
    records = StaffPage.objects \
                        .prefetch_related('roles') \
                        .exclude(staff_location='') \
                        .filter(staff_type='technical') \

    print('Found {} records of technical staff with location data '
            'to migrate.'.format(records.count()))

    for staff in records:
        # Update revisions
        if staff.has_unpublished_changes:
            # Can't use get_latest_revision() as I am unable to call
            # model methods in migrations.
            revision = staff.revisions.order_by('-created_at', '-id').first()

            if revision:
                revision_json = json.loads(revision.content_json)

                if revision_json['roles']:
                    print('Updating draft of {} (#{}).'.format(staff, staff.pk))

                    revision_json['roles'][0]['location'] = staff.staff_location

                    revision.content_json = json.dumps(revision_json)
                    revision.save()

        first_role = staff.roles.first()

        if first_role is not None:
            print('Updating live version of {} (#{}).'.format(staff, staff.pk))

            first_role.location = staff.staff_location
            first_role.save()


class Migration(migrations.Migration):
    dependencies = [
        ('rca', '0089_staffpage_move_area_and_location_field_to_roles'),
    ]

    operations = [
        migrations.RunPython(move_location_data)
    ]