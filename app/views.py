from django.shortcuts import render
from .models import foodCatogory , hotel
# Create your views here.


def home(req):

    data = foodCatogory.objects.all()
    
    hotel_detail = hotel.objects.all()
    

    return render(req,'home.html',{'category':data , 'hotel':hotel_detail})


def hotelView(req):
    hotel_detail = hotel.objects.all()
    
    return render(req,'hotel_page.html',{'hotel':hotel_detail})