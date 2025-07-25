from django.urls import path

from . import views

app_name = "checking"
urlpatterns = [
    path("" , views.index , name="index"),
    path("guest/" , views.guest , name="guest"),
    path("commodity/" , views.commodity , name="commodity"),
    path("inspecter/" , views.inspecter , name="inspecter"),
    path("guest_history/" , views.guest_history , name="guest_history"),
    path("commodity_history/" , views.commodity_history , name="commodity_history"),
    path("inspecter_history/" , views.inspecter_history , name="inspecter_history"),
    path("guest_entry/" , views.guest_entry , name="guest_entry"),
]