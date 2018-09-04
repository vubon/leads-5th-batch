from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import UserInfo


class TestView(View):

    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

    def put(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass


class Page2View(View):

    template= 'page2.html'

    def get(self, request):

        return render(request, self.template)

    def post(self, request):
        """
            {"id": 10}
        :param request:
        :return:
        """
        # data = request.data
        # UserInfo.objects.filter(pk=data['id']).delete()
        # return Response('data delete', status=
        pass


class UserDataCreateView(APIView):
    """
        URL: URI/api/v1/userinfo-create
        Method: POST
        {
            "user": "1",
            "phone": "01737388296",
            "bio":"tesfsdfdsfsdf"
        }
    """

    def post(self, request):
        request_user = request.user
        print(type(request_user))
        response, status = UserInfo.objects.user_data_create(request.data, request_user)
        return Response(response, status=status)

    def get(self, request):
        request_user = request.user
        response = UserInfo.objects.data_pull(request_user)
        return Response(response, status=status.HTTP_200_OK)
    def put(self, request):
        res = UserInfo.objects.data_update(request.user)
        return Response(res, status=status.HTTP_200_OK)

class DeleteObjectView(APIView):

    def get(self, request):
        request_user = request.user
        res = UserInfo.objects.data_delete(request_user)
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):

        res, status_code = UserInfo.objects.data_delete_pk(request.data, request.user)
        return Response(res, status=status_code)
