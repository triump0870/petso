# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PetModel',
            new_name='Pet',
        ),
    ]
