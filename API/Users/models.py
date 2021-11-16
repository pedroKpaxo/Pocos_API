from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from Helpers.UserManager import CustomUserManager

from django.db import models
from django.contrib.auth.models import PermissionsMixin, User, UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
# Create your models here.





class CustomPocoUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    profilepic = models.FileField(default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    
    

    def __str__(self):
        return self.email