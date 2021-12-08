from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
from django.utils import timezone
from utils.constants.activation import ACTIVATION_DICT


class AuthUserManager(BaseUserManager):  # Database communication interface
    def create_user(self, email, first_name, last_name):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name):
        user = self.create_user(email, first_name, last_name)

        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), null=False, blank=False, unique=True)
    password = models.CharField(_('password'), max_length=128, blank=False, null=True, default='',)

    USERNAME_FIELD = 'email'  # User identifier column
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


def get_expires_at():
    print(timezone.now() + timezone.timedelta(**ACTIVATION_DICT))
    return timezone.now() + timezone.timedelta(**ACTIVATION_DICT)


class Activation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activation')
    token = models.CharField(max_length=64, null=True, default=None, blank=False, unique=True)
    expires_at = models.DateTimeField(default=get_expires_at)
    activated_at = models.DateTimeField(null=True, default=None, blank=False)

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default='profile_images/default_image.jpg')

    @property
    def image_url(self):
        if self.avatar:

            return self.avatar.url

        return static('profile_images/default_image.jpg')
