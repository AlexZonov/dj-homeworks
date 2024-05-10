# Generated by Django 5.0.6 on 2024-05-08 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='Раздел')),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='Телефон'),
        ),
        migrations.CreateModel(
            name='ScopeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_data', to='articles.article', verbose_name='Новость')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_data', to='articles.author', verbose_name='Авторы')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_data', to='articles.scope', verbose_name='Теги')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.ScopeData', to='articles.scope', verbose_name='Теги'),
        ),
    ]