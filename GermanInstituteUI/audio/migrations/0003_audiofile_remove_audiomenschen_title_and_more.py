# Generated by Django 4.2.7 on 2024-03-23 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_rename_audiogrammatik_aktiv_audiomenschen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_title', models.CharField(max_length=255)),
                ('audio_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='audiomenschen',
            name='title',
        ),
        migrations.AddField(
            model_name='audiomenschen',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='AudioGrammatik_Aktiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('date_uploaded', models.DateField(auto_now_add=True, null=True)),
                ('audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audio.audiofile')),
            ],
        ),
        migrations.AddField(
            model_name='audiomenschen',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audio.audiofile'),
        ),
    ]
