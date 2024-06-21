from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='default_images/default.jpg')

    class Meta:
        db_table = 'Accounts'

    def __str__(self):
        return self.username
