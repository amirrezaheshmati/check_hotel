from django.urls import path

from . import views

app_name = "checking"
urlpatterns = [
    path("" , views.index , name="index"),
    path("guest/" , views.guest , name="guest"),
]