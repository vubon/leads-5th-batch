from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import datetime

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

    def post(self, request):
        response, status = UserInfo.objects.user_data_create(request.data)
        return Response(response, status=status)