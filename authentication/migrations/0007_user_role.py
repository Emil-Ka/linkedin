# Generated by Django 4.1.2 on 2022-11-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='USER', max_length=255, verbose_name='Роль'),
        ),
    ]
