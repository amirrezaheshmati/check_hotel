from django.shortcuts import render

from .models import GuestEntry
# Create your views here.
def index(request) :
    return render(request , "checking/index.html")

def guest(request) :
    return render(request , "checking/guest.html" )

def guest_history(request) :
    person = GuestEntry.objects.order_by("-date_added")
    context = {"person" : person}
    return render(request , "checking/guest_history.html" , context)

def commodity(request) :
    return render(request , "checking/commodity.html")
