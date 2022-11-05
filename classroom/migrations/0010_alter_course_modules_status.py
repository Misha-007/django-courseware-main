# Generated by Django 4.1.1 on 2022-11-05 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('module', '0004_module_assignments'),
        ('classroom', '0009_alter_course_enrolled_schedule_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(related_name='modules', to='module.module'),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
