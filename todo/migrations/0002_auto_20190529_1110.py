# Generated by Django 2.2.1 on 2019-05-29 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='title',
            new_name='checklist_name',
        ),
    ]
