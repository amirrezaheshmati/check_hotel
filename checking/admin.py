from django.contrib import admin
from .models import GuestEntry , Commodity , Inspecter
# Register your models here.
admin.site.register(GuestEntry)
admin.site.register(Commodity)
admin.site.register(Inspecter)