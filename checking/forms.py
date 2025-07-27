from django import forms

from .models import GuestEntry , Commodity , Inspecter , GuestExit , CommodityExit

class GuestEntryy(forms.ModelForm) :
    class Meta :
        model = GuestEntry
        fields = ["name" ,"pearson_code","pearson_post" ,"origin_place" ,
        "real_date_added" , "hour_added" ,"number_phone", "count" ]
        labels = {"name" : "نام و نام خانوادگی" , "real_date_added" : "تاریخ ورود", "hour_added" : "ساعت ورود",
        "number_phone" : "شماره تماس",  "pearson_code" : "کد انحصاری" , "pearson_post" : "سمت یا مقام مهمان" ,
        "origin_place" : "محل مبدا" , "count" : "تعداد افراد"}
        
class CommodityEntry(forms.ModelForm) :
    class Meta :
        model = Commodity
        fields = ["name" , "code" ,"real_date_added" , "hour_added" ,
        "count" , "descript"]
        labels = {"name" : "اسم", "real_date_added" :"تاریخ ورود" , "hour_added" : "ساعت ورود"
        ,"code" : "کد اموالی" , "descript" : "توضیحات" , "count" : "تعداد اقلام"}
    
class InspecterEntry(forms.ModelForm) :
    class Meta :
        model = Inspecter
        fields = ["name" ,"pearsone_post" ,"origin_place" , "real_date_added" ,
        "hour_added","date_exit" , "hour_exit" ,"number_phone" ,"descript" ]
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