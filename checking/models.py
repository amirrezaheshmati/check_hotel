from django.db import models

# Create your models here.
#guest , inspecter , commodity

class GuestEntry(models.Model) :
    name = models.CharField(max_length=60)
    real_date_added = models.DateTimeField(auto_now_add=True)
    date_added = models.CharField(max_length=15)
    hour_added = models.IntegerField()
    number_phone = models.CharField(max_length=11)
    pearson_code = models.CharField(max_length=10)
    pearson_post = models.CharField(max_length=60)
    origin_place = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Commodity(models.Model) :
    name = models.CharField(max_length=60)
    real_date_added = models.DateTimeField(auto_now_add=True)
    date_added = models.CharField(max_length=15)
    hour_added = models.IntegerField()
    code = models.CharField(max_length=10)
    descript = models.TextField()
    
    def __str__(self):
        return self.name

class Inspecter(models.Model) :
    name = models.CharField(max_length=60)
    real_date_added = models.DateTimeField(auto_now_add=True)
    date_added = models.CharField(max_length=15)
    hour_added = models.IntegerField()
    number_phone = models.CharField(max_length=11)
    pearsone_post = models.CharField(max_length=60)
    origin_place = models.CharField(max_length=30)
    descript = models.TextField()
    
    def __str__(self):
        return self.name