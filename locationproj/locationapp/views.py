from multiprocessing import context
from django.shortcuts import render, redirect
import smtplib,ssl,email
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
            verified = True
            user = email.split('@')[0]
            request.session['user'] = user
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
    #if request.method == "POST":
        #return render(request,"home.html")
    
    return render(request,"register.html")


from email.mime.text import MIMEText
def validate(request):
    recv = request.POST.get('email')
    try:
        obj = userdetail.objects.get(email=recv)
        print("object : ",obj.email)
        return render(request,"register.html",{"msg":"user already exists.."})
    except :
        s = smtplib.SMTP('smtp.gmail.com',587)
        msg = """\
            <html>
            <h1>Authenticate<h1><br>
            <h2>This message was sent by glacial-badlands-23822</h2><br>
            <h2>To register for this site please click the below link</h2>
            
            <h4><a href="http://127.0.0.1:8000/verify/{},{},{},{}">verify its you</a></h4>
            
            </html>""".format(request.POST.get('uname'),
                       request.POST.get('pswd'),
                       str(request.POST.get('phn')),
                       request.POST.get('email'))
        
        msg = MIMEText(msg,'html')
        context = ssl.create_default_context()
        s.starttls(context=context)
        s.login('backbenchers143.rgm@gmail.com','lgwnnimpsvzbblue')
    
        s.sendmail('backbenchers143.rgm@gmail.com',recv,msg.as_string())
        s.quit()
        return render(request,"login.html",{"error" : "Gmail was sent to you"})
def verify(request,info):
    l = info.split(',')
    username = l[0]
    password = l[1]
    phn = l[2]
    email = l[3]
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
    """.format(username,password,phn,email)
    msg = MIMEText(msg,'html')
    context = ssl.create_default_context()
    s.starttls(context=context)
    s.login('backbenchers143.rgm@gmail.com','lgwnnimpsvzbblue')
    s.sendmail('backbenchers143.rgm@gmail.com',['lucky630584@gmail.com',email],msg.as_string())
    s.quit()
    return render(request,"login.html",{"error":"your account activated...<br> login into your account"})
    
    
    