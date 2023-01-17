# Generated by Django 4.1.2 on 2022-12-30 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testing', '0005_test_desc_alter_test_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='desc',
            field=models.TextField(verbose_name='Описание теста'),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Выбранный вариант ответа',
                'verbose_name_plural': 'Выбранные варианты ответа',
            },
        ),
    ]