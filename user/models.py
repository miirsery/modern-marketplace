from django.urls import reverse
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from imagekit.models import ProcessedImageField
# Create your models here.


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
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True,
        verbose_name="URL", null=True
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
    is_active = models.BooleanField(
        default=True,
        verbose_name='Является активным'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Является админом'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
