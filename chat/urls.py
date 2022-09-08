from django.urls import path
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('',views.join,name="join"),
    path('room/<str:name>',views.room,name="room"),
    path('check',views.check,name="check"),
    path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    #path('r/<str:username>',views.room,name="re/")
]
