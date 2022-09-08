import re
from django.shortcuts import render, redirect

# Create your views here.
def join(request):
    if request.method == "POST":
        return render(request,"room.html")
    else:
        return render(request,"join.html")
def room(request,name):
    if request.method == "GET":
        username = name
        return render(request,'room.html',{'name':username})
    return render(request,'room.html',{'name':'user'})
    
    
def check(request):
    if request.method == "GET":
        username = request.GET['name']
        return redirect('room',username)
    if request.method == "POST":
        username = request.POST['username']
        #return render(request,'room.html',{'name':username})
        return redirect('room',username)