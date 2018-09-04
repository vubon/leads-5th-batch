from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestView.as_view()),
    path('page/', views.Page2View.as_view()),
    path('data-create', views.UserDataCreateView.as_view()),
    path('delete-data', views.DeleteObjectView.as_view()),
]
