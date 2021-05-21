from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True)
    word_expiry_days = models.IntegerField(default=7)

    def __str__(self):
        return self.user.username
