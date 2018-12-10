from django.urls import path, include
from . import views

app_name = "QMLove"
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('', include('django.contrib.auth.urls')),
  
]
