from django.urls import path
from . import views

urlpatterns = [
    path('',views.join,name="join"),
    path('room/<str:name>',views.room,name="room"),
    path('check',views.check,name="check"),
    #path('r/<str:username>',views.room,name="re/")
]
