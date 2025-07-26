from django import forms

from .models import GuestEntry , Commodity , Inspecter

class GuestEntryy(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        fields = ["name" , "real_date_added" , "hour_added" ,
        "number_phone", "pearson_code" , "pearson_post" , "origin_place"]
        labels = {"name" : "نام و نام خانوادگی" , "real_date_added" : "تاریخ ورود", "hour_added" : "ساعت ورود",
        "number_phone" : "شماره تماس",  "pearson_code" : "کد انحصاری" , "pearson_post" : "سمت یا مقام مهمان" ,
        "origin_place" : "محل مبدا"}
        
class CommodityEntry(forms.ModelForm) :
    class Meta :
        model = Commodity
        fields = ["name" , "real_date_added" , "hour_added" ,
        "code" , "descript"]
        labels = {"name" : "اسم", "real_date_added" :"تاریخ ورود" , "hour_added" : "ساعت ورود"
        ,"code" : "کد انحصاری" , "descript" : "توضیحات"}
    
class InspecterEntry(forms.ModelForm) :
    class Meta :
        model = Inspecter
        fields = ["name" , "real_date_added" , "hour_added",
        "pearsone_post" , "number_phone" , "origin_place" , "descript"]
        labels = {"name" : "نام و نام خانوادگی", "real_date_added" :"تاریخ ورود" , "hour_added" : "ساعت ورود",
        "pearsone_post" : "سمت یا مقام بازرس", "number_phone" :"شماره تماس" ,
        "origin_place" : "محل مبدا", "descript" : "توضیحات"}

class ExitTimeGuest(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        fields = ["date_exit"]
        labels = {"date_exit" : "تاریخ خروج"}
        
class ExitTimeCommedity(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        fields = ["date_exit"]
        labels = {"date_exit" : "تاریخ خروج"}