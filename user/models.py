from django.urls import reverse
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ProcessedImageField


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Логин пользователя', max_length=50,
        unique=True,
    )
    slug = AutoSlugField(
        populate_from='username'
    )
    email = models.EmailField(max_length=100, unique=True)
    avatar = ProcessedImageField(
        upload_to='avatars',
        format='JPEG',
        verbose_name='Аватарка пользователя',
        blank=True,
        null=True,
        default='system_images/defult.jpg',
    )
    firts_name = models.CharField(
        verbose_name='Имя',
        max_length=255,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=255,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Является активным'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Является админом'
    )
    is_moderator = models.BooleanField(
        default=False,
        verbose_name='Является моддератором'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    role = models.CharField(
        verbose_name='Основная роль пользователя',
        max_length=255,
        default='user'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.is_active is True and self.is_staff is False\
                and self.is_moderator is False:
            self.role = 'user'
        elif self.is_active is True and self.is_moderator is True\
                and self.is_staff is False:
            self.role = 'moderator'
        elif self.is_active is True and self.is_staff is True\
                and self.is_moderator is False:
            self.role = 'admin'
        elif self.is_active is True and self.is_staff is True\
                and self.is_moderator is True:
            self.role = 'admin'
        else:
            self.role = 'anonymous_user'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
