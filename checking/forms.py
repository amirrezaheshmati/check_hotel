from django import forms

from .models import GuestEntry

class GuestEntryy(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        #name = forms.CharField(max_length=60)
        #real_date_added = forms.CharField(max_length=15)
        #hour_added = forms.IntegerField()
        #number_phone = forms.CharField(max_length=11)
        #pearson_code = forms.CharField(max_length=10)
        #pearson_post = forms.CharField(max_length=60)
        #origin_place = forms.CharField(max_length=30)
        fields = ["name" , "real_date_added" , "hour_added" ,
        "number_phone", "pearson_code" , "pearson_post" , "origin_place"]
        labels = {"name" : "name" , "real_date_added" : "date added", "hour_added" : "hour added",
        "number_phone" : "number phone",  "pearson_code" : "pearson code" , "pearson_post" : "pearson post" , "origin_place" : "origin place"}