# Generated by Django 5.0.3 on 2024-05-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='students.course'),
        ),
    ]
