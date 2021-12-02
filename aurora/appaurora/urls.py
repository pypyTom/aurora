from django.urls import path
from appaurora import views



urlpatterns = [
path('', views.index, name='index')
]