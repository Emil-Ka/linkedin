# Generated by Django 4.1.2 on 2023-01-07 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_alter_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Email')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('photo', models.TextField(max_length=100, null=True, verbose_name='Фото')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'USER'), (1, 'HR'), (2, 'ADMIN')])),
                ('is_active', models.BooleanField(default=False, verbose_name='Активирован')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Администратор')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Пользователь',
                'verbose_name_plural': 'historical Пользователи',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]