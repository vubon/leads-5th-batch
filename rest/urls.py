from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestView.as_view()),
    path('page/', views.Page2View.as_view()),
]
