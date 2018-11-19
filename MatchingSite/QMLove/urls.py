from django.urls import path
from . import views

app_name = "QMLove"
urlpatterns = [
    path('', views.index, name="index"),
]
