from django.contrib import admin

from .models import food ,foodCatogory,hotel




class foodview(admin.ModelAdmin):
    list_display=('name','hotel_name','catogory','rating','combo',)



class hotelmodel(admin.ModelAdmin):
    list_display =('name','rating','city')


admin.site.register(food,foodview)
admin.site.register(foodCatogory)
admin.site.register(hotel,hotelmodel)