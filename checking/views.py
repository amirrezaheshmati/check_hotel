from django.shortcuts import render

from .models import GuestEntry
# Create your views here.
def index(request) :
    return render(request , "checking/index.html")

def guest(request) :
    return render(request , "checking/guest.html" )