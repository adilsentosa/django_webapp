# Generated by Django 3.2.8 on 2021-11-12 10:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_rename_bioadata_biodata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Biodata',
            new_name='Datadiri',
        ),
        migrations.AlterModelOptions(
            name='datadiri',
            options={'verbose_name_plural': 'Datadiri'},
        ),
    ]
