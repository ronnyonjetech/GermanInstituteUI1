# Generated by Django 4.2.7 on 2024-03-22 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AudioGrammatik_Aktiv',
            new_name='AudioMenschen',
        ),
        migrations.DeleteModel(
            name='AudioMenschen_A1',
        ),
        migrations.DeleteModel(
            name='AudioMenschen_A2',
        ),
        migrations.DeleteModel(
            name='AudioMenschen_B1',
        ),
    ]
