from django.shortcuts import render
import json
import urllib.request 
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,"index.html")
def wheather(request):
    if request.method == "POST":
        country_name = request.POST['cityname']
        try : 
            res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+country_name+"&appid=be3bf8077d812ff89e61c62638e29687").read()
            json_data = json.loads(res)
            data = {
                "country_code" : str(json_data['sys']['country']),
                "temp"         : str(json_data['main']['temp']),
                "preasure"     : str(json_data['main']['pressure']),
                "humidity"     : str(json_data['main']['humidity'])
            }
            data["temp"] = str("{:.2f}".format(float(data["temp"])-273.15))+" c"
            return render(request,"wheather.html",data)
        except Exception as e:
            messages.info(request,e)
            messages.info(request,"city not found.....")
            return render(request,"wheather.html")
                
        
    else:
        data = {
            
        }
        return render(request,"wheather.html")