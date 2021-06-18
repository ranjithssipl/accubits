from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from simple_history.models import HistoricalRecords
from django.conf import settings

# Create your models here.


class AccubitsUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    last_name = models.CharField(null=True, max_length=150)
    name = models.CharField(max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']



