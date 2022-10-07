from multiprocessing import context
from django.shortcuts import render, redirect
import smtplib,ssl
#from django.contrib.gis.geoip2 import GeoIP2
from .models import userdetail
# Create your views here.

def index(request):
    return render(request, "index.html")

def track(request):
    return render(request,"trackme.html")
def otpverification(request):
    return render(request,"otpverification.html")
def login(request,coor):
    global lat, lon
    
    if request.method == "POST":
        verified = False
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')       
        try:
            obj = userdetail.objects.get(email=email)
            print(obj.password)
            verified = True
        except:
            print("invalid")
        if verified:
            check = False
            #check = check_coor(request,obj)
            latitude = float(obj.latitude)
            lat = float(request.session['lat'])
            longitude = float(obj.longitude)
            lon = float(request.session['lon'])
            if latitude >= lat:
                res1 = latitude - lat
                if longitude >= lon:
                    res2 = longitude - lon
                else:
                    res2 = lon - longitude
            else:
                res1 = lat - latitude
                if longitude >= lon:
                    res2 = longitude - lon
                else:
                    res2 = lon - longitude
            print(res1,res2,res1+res2)
            if (res1+res2) < 0.3:
                print("location verified...")
                check = True
            else:
                return render(request,"login.html",{"error" : "you are out of location, auth is required","link": "authenticate"})

            if obj.password == pswd and check:
                
                #finally login 
                return render(request,"home.html")
        return render(request,"login.html",{"error": "you are not registered or wrong email id"})
    else:
        l = coor.split("&&")
        print(l)
        lat, lon = l[0],l[1]
        request.session['lat'] = lat
        request.session['lon'] = lon
        en = request.GET.get('encode')
        de = ""
        for i in en:
            de+=chr(ord(i)-3)
        if de == "true":
            print("accessed")
            return render(request,"login.html",{"lat": lat,"lon":lon})
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
        obj.latitude = request.session['lat']
        obj.longitude = request.session["lon"]
        obj.save()
        s = smtplib.SMTP('smtp.gmail.com',587)
        msg = """\
        Account created\n
        
        username : {}\n
        password : {}\n
        phone    : {}\n
        email    : {} 
        """+username+" "+password+" "+phn+" "+email
        context = ssl.create_default_context()
        s.starttls(context=context)
        s.login('backbenchers143.rgm@gmail.com','lgwnnimpsvzbblue')
        s.sendmail('backbenchers143.rgm@gmail.com',['lucky630584@gmail.com',email],msg)
        s.quit()
        return render(request,"home.html")
    
    return render(request,"register.html")