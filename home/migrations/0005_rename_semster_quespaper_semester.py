# Generated by Django 3.2.3 on 2021-05-18 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_subjects_subject_sub_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quespaper',
            old_name='semster',
            new_name='semester',
        ),
    ]
