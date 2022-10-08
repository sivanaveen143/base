from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('track',views.track,name="track"),
    path('web/validate',views.validate,name="validate"),
    path('web/register',views.register,name="register"),
    path('web/enterotp',views.otpverification,name="otpverification"),
    path('/<str:coor>',views.login, name="login"),
    path('verify/<str:info>',views.verify,name="verify")
    
]
