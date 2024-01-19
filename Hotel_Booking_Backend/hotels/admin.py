from django.contrib import admin
from .models import Hotel,Room,Image,Reservation
# Register your models here.

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Image)
admin.site.register(Reservation)