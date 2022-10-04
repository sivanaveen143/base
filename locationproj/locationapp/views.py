from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.
def index(request):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        ip = x_forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2()
    lat, lon = g.lat_lon(ip)
    print(lat, lon)
    print(ip)
    return render(request, "index.html",{"lon" : float(lon),"lat":float(lat)})