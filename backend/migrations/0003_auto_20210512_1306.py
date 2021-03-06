# Generated by Django 3.2.2 on 2021-05-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projects',
            name='github',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='projects',
            name='live',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
