from django.db import models
import jdatetime
from django.contrib.auth.models import User
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
    pearson_post = models.CharField(max_length=60 , default="")
    origin_place = models.CharField(max_length=30 , default="تبریز")
    show_in_list = models.BooleanField(default=True)
    owner_gue_c = models.ForeignKey(User , on_delete=models.CASCADE,related_name="gue_c" , null=True , blank=True )
    
    def __str__(self):
        return self.name

class GuestExit(models.Model) :
    guest = models.ForeignKey(GuestEntry , on_delete=models.CASCADE , related_name="exit")
    now = jdatetime.datetime.now()
    hour_exit = models.IntegerField(default=int(now.strftime("%H")))
    date_exit = models.CharField(max_length=15 , default=str(jdatetime.datetime.now().strftime("%Y/%m/%d")))
    owner_gue_d = models.ForeignKey(User , on_delete=models.CASCADE,related_name="gue_d" , null=True , blank=True)

class Commodity(models.Model) :
    now = jdatetime.datetime.now()
    name = models.CharField(max_length=60)
    real_date_added = models.CharField(max_length=15 ,default=str(now.strftime("%Y/%m/%d")))
    date_added = models.DateTimeField(auto_now_add=True)
    hour_added = models.IntegerField(default=int(now.strftime("%H")))
    code = models.CharField(max_length=10)
    descript = models.TextField()
    show_in_list = models.BooleanField(default=True)
    owner_com_c = models.ForeignKey(User , on_delete=models.CASCADE , related_name="com_c", null=True , blank=True)
    
    def __str__(self):
        return self.name

class CommodityExit(models.Model) :
    commodity = models.ForeignKey(Commodity , on_delete=models.CASCADE , related_name="exit_com")
    now = jdatetime.datetime.now()
    hour_exit = models.IntegerField(default=int(now.strftime("%H")))
    date_exit = models.CharField(max_length=15 , default=str(now.strftime("%Y/%m/%d")))
    owner_com_d = models.ForeignKey(User , on_delete=models.CASCADE , related_name="com_d" , null=True , blank=True)

class Inspecter(models.Model) :
    now = jdatetime.datetime.now()
    name = models.CharField(max_length=60)
    real_date_added = models.CharField(max_length=15 ,default=str(now.strftime("%Y/%m/%d")))
    date_added = models.DateTimeField(auto_now_add=True)
    hour_added = models.IntegerField(default=int(now.strftime("%H")))
    number_phone = models.CharField(max_length=11 , default="09")
    pearsone_post = models.CharField(max_length=60, default="")
    origin_place = models.CharField(max_length=30 , default="تبریز")
    descript = models.TextField()
    date_exit = models.CharField(max_length=15 , default=str(jdatetime.datetime.now().strftime("%Y/%m/%d")))
    hour_exit = models.IntegerField(default=int(now.strftime("%H")))
    owner_ins_c = models.ForeignKey(User , on_delete=models.CASCADE , related_name="ins_c")
    
    def __str__(self):
        return self.name