# Generated by Django 4.1.2 on 2023-01-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_historicalvacancy_historicalresume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Описание резюме'),
        ),
        migrations.AddField(
            model_name='resume',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Описание резюме'),
        ),
        migrations.AddField(
            model_name='resume',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок резюме'),
        ),
        migrations.AddField(
            model_name='resume',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок резюме'),
        ),
    ]
