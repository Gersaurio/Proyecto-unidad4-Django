# Generated by Django 4.1.4 on 2022-12-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('photo', models.URLField()),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(null=True)),
                ('tags', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'repositorio',
            },
        ),
    ]
