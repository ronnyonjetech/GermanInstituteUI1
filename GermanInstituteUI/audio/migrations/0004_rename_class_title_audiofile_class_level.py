# Generated by Django 4.2.7 on 2024-03-23 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_audiofile_remove_audiomenschen_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiofile',
            old_name='class_title',
            new_name='class_level',
        ),
    ]