from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager
from authentication.roles import ROLE_CHOICES


class User(AbstractBaseUser, PermissionsMixin):
    # verbose_name - как будет отображаться в админке
    # upload_to - будет загружать в media/users/photo/img.jpg
    # USERNAME_FIELD - уникальная идентификация по Email
    # is_active - активирован или нет (по паролю на почте и т.д.)
    # is_staff - сотрудник (имеет частичный доступ к админке)
    # is_superuser - админ или нет
    # __str__ - как будет выводится модель в админке
    # Meta: verbose_name - когда 1 сущность, verbose_name_plural - когда несколько

    email = models.EmailField(verbose_name='Email',max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/photo')
    bio = models.TextField(verbose_name='О себе', blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)

    is_active = models.BooleanField(verbose_name='Активирован', default=False)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
