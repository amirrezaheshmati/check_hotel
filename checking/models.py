from django.db import models
import jdatetime
# Create your models here.
#guest , inspecter , commodity

class GuestEntry(models.Model) :
    now = jdatetime.datetime.now()
    name = models.CharField(max_length=60)
    real_date_added = models.CharField(max_length=15 ,default=str(now.strftime("%Y/%m/%d")))
    date_added = models.DateTimeField(auto_now_add=True)
    hour_added = models.IntegerField(default=int(now.strftime("%H")))
    number_phone = models.CharField(max_length=11 , default="09")
    pearson_code = models.CharField(max_length=10)
    pearson_post = models.CharField(max_length=60 , default=" ")
    origin_place = models.CharField(max_length=30 , default="Tabriz")
    show_in_list = models.BooleanField(default=True)
    date_exit = models.CharField(max_length=15 , default=str(jdatetime.datetime.now().strftime("%Y/%m/%d")))
    #date_exit = models.
    
    def __str__(self):
        return self.name

class Commodity(models.Model) :
    now = jdatetime.datetime.now()
    name = models.CharField(max_length=60)
    real_date_added = models.CharField(max_length=15 ,default=str(now.strftime("%Y/%m/%d")))
    date_added = models.DateTimeField(auto_now_add=True)
    hour_added = models.IntegerField(default=int(now.strftime("%H")))
    code = models.CharField(max_length=10)
    descript = models.TextField()
    show_in_list = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Inspecter(models.Model) :
    now = jdatetime.datetime.now()
    name = models.CharField(max_length=60)
    real_date_added = models.CharField(max_length=15 ,default=str(now.strftime("%Y/%m/%d")))
    date_added = models.DateTimeField(auto_now_add=True)
    hour_added = models.IntegerField(default=int(now.strftime("%H")))
    number_phone = models.CharField(max_length=11 , default="09")
    pearsone_post = models.CharField(max_length=60, default=" ")
    origin_place = models.CharField(max_length=30 , default="Tabriz")
    descript = models.TextField()
    date_exit = models.CharField(max_length=15 , default=str(jdatetime.datetime.now().strftime("%Y/%m/%d")))
    
    def __str__(self):
        return self.name