# Generated by Django 4.1.4 on 2022-12-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repoapp', '0002_alter_projects_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='updated_at',
        ),
    ]
