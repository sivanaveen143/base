from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('/register',views.register,name="register"),
    path('/enterotp',views.otpverification,name="otpverification"),
    path('/<str:coor>',views.login, name="login"),
]
