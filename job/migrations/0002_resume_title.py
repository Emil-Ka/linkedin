# Generated by Django 4.1.2 on 2022-11-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='title',
            field=models.CharField(default='Резюме', max_length=255, verbose_name='Заголовок резюме'),
        ),
    ]
