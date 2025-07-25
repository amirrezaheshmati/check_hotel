from django.shortcuts import render , redirect
from .forms import GuestEntryy , CommodityEntry , InspecterEntry

from .models import GuestEntry , Commodity , Inspecter
# Create your views here.
def index(request) :
    return render(request , "checking/index.html")

def guest(request) :
    return render(request , "checking/guest.html" )

def commodity(request) :
    return render(request , "checking/commodity.html")

def inspecter(request) :
    return render(request , "checking/inspecter.html")

def guest_history(request) :
    person = GuestEntry.objects.order_by("-date_added")
    context = {"person" : person}
    return render(request , "checking/guest_history.html" , context)

def commodity_history(request) :
    pearson = Commodity.objects.order_by("-date_added")
    context = {"pearson" : pearson}
    return render(request , "checking/commodity_history.html" , context)

def inspecter_history(request) :
    pearson = Inspecter.objects.order_by("-date_added")
    context = {"pearson" : pearson}
    return render(request , "checking/inspecter_history.html" , context)

def guest_entry(request) :
    if request.method != "POST" :
        form = GuestEntryy()
    else : 
        form = GuestEntryy(data = request.POST)
        if form.is_valid() :
            form.save()
            return redirect("checking:guest")
    
    context = {"form" : form}
    return render(request, "checking/guest_entry.html" , context)

def commodity_entry(request) :
    if request.method != "POST":
        form = CommodityEntry()
    else :
        form = CommodityEntry(data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect("checking:commodity")
    
    context = {"form" : form}
    return render(request , "checking/commodity_entry.html" , context)

def inspecter_entry(request) :
    if request.method != "POST" :
        form = InspecterEntry()
    else :
        form = InspecterEntry(data= request.POST)
        if form.is_valid() :
            form.save()
            return redirect("checking:inspecter")
    
    context = {"form" : form}
    return render(request , "checking/inspecter_entry.html" , context)
