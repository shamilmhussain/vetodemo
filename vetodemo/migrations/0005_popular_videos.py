# Generated by Django 2.2 on 2019-04-30 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vetodemo', '0004_auto_20190422_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vetodemo.Category')),
            ],
        ),
    ]
