from django import forms

from .models import GuestEntry , Commodity , Inspecter , GuestExit , CommodityExit

class GuestEntryy(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        fields = ["name" ,"pearson_code","pearson_post" ,"origin_place" ,
        "real_date_added" , "hour_added" ,"number_phone",  ]
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
        "pearsone_post" , "number_phone" , "origin_place" , "date_exit" , "hour_exit" ,"descript" ]
        labels = {"name" : "نام و نام خانوادگی", "real_date_added" :"تاریخ ورود" , "hour_added" : "ساعت ورود",
        "pearsone_post" : "سمت یا مقام بازرس", "number_phone" :"شماره تماس" ,
        "origin_place" : "محل مبدا", "date_exit" : "تازیخ خروج" , "hour_exit" : "ساعت خروج" , "descript" : "توضیحات"}

class ExitTimeGuest(forms.ModelForm) :
    class Meta :
        model = GuestExit
        fields = ["date_exit" , "hour_exit"]
        labels = {"date_exit" : "تاریخ خروج" , "hour_exit" : "ساعت خروج"}
        
class ExitTimeCommedity(forms.ModelForm) :
    class Meta :
        model = CommodityExit
        fields = ["date_exit" , "hour_exit"]
        labels = {"date_exit" : "تاریخ خروج" , "hour_exit" : "ساعت خروج"}