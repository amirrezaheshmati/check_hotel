from django import forms

from .models import GuestEntry , Commodity

class GuestEntryy(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        fields = ["name" , "real_date_added" , "hour_added" ,
        "number_phone", "pearson_code" , "pearson_post" , "origin_place"]
        labels = {"name" : "name" , "real_date_added" : "date added", "hour_added" : "hour added",
        "number_phone" : "number phone",  "pearson_code" : "pearson code" , "pearson_post" : "pearson post" , "origin_place" : "origin place"}
        
class CommodityEntry(forms.ModelForm) :
    class Meta :
        model = Commodity
        fields = ["name" , "real_date_added" , "hour_added" ,
        "code" , "descript"]
        labels = {"name" : "name", "real_date_added" :"date" , "hour_added" : "hour"
        ,"code" : "code" , "descript" : "descript"}