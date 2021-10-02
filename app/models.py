from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    second_name = models.CharField(verbose_name='Отчество',
                                   max_length=33, null=True)
