# Generated by Django 4.1.1 on 2022-11-05 05:59

import assignment.models
import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentfilecontent',
            name='file',
            field=models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to=assignment.models.user_directory_path),
        ),
    ]
