# Generated by Django 4.1.2 on 2022-12-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='users/photo', verbose_name='Фото'),
        ),
    ]