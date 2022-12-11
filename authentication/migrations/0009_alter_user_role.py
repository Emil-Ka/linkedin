# Generated by Django 4.1.2 on 2022-11-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'USER'), (2, 'HR'), (3, 'ADMIN')], default=1),
        ),
    ]