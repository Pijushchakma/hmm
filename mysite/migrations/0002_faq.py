# Generated by Django 3.0.6 on 2020-08-08 08:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('approve', models.NullBooleanField(default=None)),
            ],
        ),
    ]