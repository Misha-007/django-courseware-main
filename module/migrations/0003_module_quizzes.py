# Generated by Django 3.2 on 2021-05-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        ('module', '0002_module_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='quizzes',
            field=models.ManyToManyField(to='quiz.Quizzes'),
        ),
    ]
