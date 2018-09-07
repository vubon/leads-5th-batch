from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserInfoManager(models.Manager):
    """
        Description
    """

    def user_data_create(self, data, request_user):
        """
        - data validation
        - if not pass data validation raise error
        - if pass data validation
        - create
        :param data:
        :param request_user:
        :return: msg and status code
        :rtype: tuple
        """
        phone = data['phone']

        if len(phone) ==11:
            phone_number = phone
        else:
            msg = {"message": "invalid phone number"}
            status_code = 400
            return msg, status_code

        self.create(
            user=request_user,
            phone_number=phone_number,
            bio=data['bio'],
            time=timezone.now()
        )
        msg = {"message": "Data created"}
        status_code = 201
        return msg, status_code

    def data_pull(self, request_user):
        """
        :return:
        """
        return self.filter(
            user=request_user
        ).values(
            'id',
            'user__username',
            'user__date_joined',
            'user__email',
            'user__last_login',
            'phone_number',
            'bio',
            'time'
        )

    def data_delete(self, request_user):
        delete_obj = self.filter(user=request_user)
        delete_obj.delete()

        msg = {"message": "Delete success"}
        return msg

    def data_delete_pk(self, pk, request_user):
        if not self.filter(pk=pk['id']).exists():
            return {"message": "Invalid ID"}, 400

        delete_obj = self.filter(pk=pk['id'], user=request_user)

        if not delete_obj:
            return {"message": "Invalid ID"}, 400

        delete_obj.delete()
        msg = {"message": "Delete success"}
        return msg , 200

    def data_update(self, request_user):
        self.filter(user=request_user).update(
            
        )
    # Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    bio = models.TextField(max_length=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    objects = UserInfoManager()

    def __str__(self):
        return str(self.user.first_name)
