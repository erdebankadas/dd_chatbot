from django.urls import path
from ddchatapp import views

urlpatterns = [
    path('', views.chat, name='chat'),
]
