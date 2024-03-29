# Generated by Django 2.1 on 2019-07-09 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190709_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TimeStampModel',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('timestampmode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.TimeStampMode')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=10, unique=True)),
            ],
            bases=('posts.timestampmode',),
        ),
    ]
