from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, UserManager, PermissionsMixin
import uuid
from django.utils import timezone

# Create your models here.

class AccountUserManager(BaseUserManager):
    """
        This is a manager for Account class
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=30, default=None, blank=True, null=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['username']
    objects = AccountUserManager()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    def has_module_perms(self, app_label):
        return True



