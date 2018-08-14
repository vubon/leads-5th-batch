from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    bio = models.TextField(max_length=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.user.first_name)