# Generated by Django 5.0.4 on 2024-05-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Зонов А.В.', max_length=50, verbose_name='Автор'),
        ),
    ]
