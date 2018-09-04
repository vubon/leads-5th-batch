from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserInfoManager(models.Manager):
    """
        Description
    """

    def user_data_create(self, data):
        """
        - data validation
        - if not pass data validation raise error
        - if pass data validation
        - create
        :param data:
        :return: msg and status code
        :rtype: tuple
        """
        self.create(
            user_id=data['user'],
            phone_number=data['phone'],
            bio=data['bio'],
            time=timezone.now()
        )
        msg = {"message": "Data created"}
        status_code = 201
        return msg, status_code

    def test(self):
        pass

    # Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    bio = models.TextField(max_length=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    objects = UserInfoManager()

    def __str__(self):
        return str(self.user.first_name)
