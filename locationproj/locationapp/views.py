from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
from .models import userdetail
# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request,coor):
    global lat, lon
    print(request.method)
    if request.method == "POST":
        print("post method")
        print(lat,lon)
        return redirect("index")
    else:
        l = coor.split("&&")
        print(l)
        lat, lon = l[0],l[1]
        en = request.GET.get('encode')
        de = ""
        for i in en:
            de+=chr(ord(i)-3)
        if de == "true":
            print("accessed")
            return render(request,"login.html")
        return render(request,"index.html",{"error" : "for login or register please make sure to enable location"})
def register(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        phn = request.POST.get('phn')
        email = request.POST.get('email')
        obj = userdetail()
        obj.username = username
        obj.password = password
        obj.phone = phn
        obj.email = email
        obj.latitude = lat
        obj.longitude = lon
        obj.save()
        return render(request,"home.html")
    
    return render(request,"register.html")