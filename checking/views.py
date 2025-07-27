from django.shortcuts import render , redirect 
from .forms import GuestEntryy , CommodityEntry , InspecterEntry , ExitTimeGuest , ExitTimeCommedity
import jdatetime

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
            new_guest = form.save(commit=False)
            new_guest.owner_gue_c = request.user
            new_guest.save()
            return redirect("checking:guest")
    
    context = {"form" : form}
    return render(request, "checking/guest_entry.html" , context)

def commodity_entry(request) :
    if request.method != "POST":
        form = CommodityEntry()
    else :
        form = CommodityEntry(data=request.POST)
        if form.is_valid() :
            new_commedity = form.save(commit=False)
            new_commedity.owner_com_c = request.user
            new_commedity.save()
            return redirect("checking:commodity")
    
    context = {"form" : form}
    return render(request , "checking/commodity_entry.html" , context)

def inspecter_entry(request) :
    if request.method != "POST" :
        form = InspecterEntry()
    else :
        form = InspecterEntry(data= request.POST)
        if form.is_valid() :
            new_inspecter = form.save(commit=False)
            new_inspecter.owner_ins_c = request.user
            new_inspecter.save()
            return redirect("checking:inspecter")
    
    context = {"form" : form}
    return render(request , "checking/inspecter_entry.html" , context)

def guest_list(request) :
    pearson = GuestEntry.objects.order_by("date_added").filter(show_in_list=True)
    context = {"pearson" : pearson}
    return render(request , "checking/guest_list.html" , context)

def commedity_list(request) :
    pearson = Commodity.objects.order_by("date_added").filter(show_in_list=True)
    context = {"pearson" : pearson}
    return render(request , "checking/commedity_list.html" , context)

def delete_guest(request , guest_id) :
    pearson = GuestEntry.objects.get(id=guest_id)
    if request.method != "POST" :
        form = ExitTimeGuest()
    else :
        form = ExitTimeGuest(data=request.POST)
        if form.is_valid() :
            exit_instance = form.save(commit=False)
            exit_instance.guest = pearson
            exit_instance.owner_gue_d = request.user
            exit_instance.save()
            pearson.show_in_list = False
            pearson.save()
            return redirect("checking:guest_list")
    context = {"pearson" : pearson , "form" : form}
    return render(request , "checking/delete_guest.html" , context)

def delete_commedity(request , commedity_id) :
    pearson = Commodity.objects.get(id= commedity_id)
    if request.method != 'POST' :
        form = ExitTimeCommedity()
    else :
        form = ExitTimeCommedity(data=request.POST)
        if form.is_valid() :
            exit_instance = form.save(commit=False)
            exit_instance.commodity = pearson
            exit_instance.owner_com_d = request.user
            exit_instance.save()
            pearson.show_in_list = False
            pearson.save()
            return redirect("checking:commedity_list")
    context = {"pearson" : pearson , "form" : form}
    return render(request , "checking/delete_commedity.html" , context)