# Generated by Django 4.1.2 on 2022-11-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_resume_salary_alter_vacancy_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.FloatField(null=True, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(null=True, verbose_name='Зарплата'),
        ),
    ]
