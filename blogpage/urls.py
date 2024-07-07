from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
   
    
]