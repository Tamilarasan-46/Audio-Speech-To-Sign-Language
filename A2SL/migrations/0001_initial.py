# Generated by Django 3.2.25 on 2025-02-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_url', models.URLField()),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10)),
            ],
        ),
    ]
