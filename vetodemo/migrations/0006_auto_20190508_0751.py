# Generated by Django 2.2 on 2019-05-08 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetodemo', '0005_popular_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='category',
        ),
        migrations.RemoveField(
            model_name='module_type',
            name='category',
        ),
        migrations.RemoveField(
            model_name='module_type',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='module_type',
            name='level',
        ),
        migrations.RemoveField(
            model_name='module_type',
            name='module',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='category',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='level',
        ),
        migrations.RemoveField(
            model_name='sub_modules',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sub_modules',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='sub_modules',
            name='level',
        ),
    ]
