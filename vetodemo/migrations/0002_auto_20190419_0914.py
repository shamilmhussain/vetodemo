# Generated by Django 2.2 on 2019-04-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetodemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_model',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_model',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
