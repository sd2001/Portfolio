# Generated by Django 3.2.2 on 2021-06-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_picture_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='github',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projects',
            name='live',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
