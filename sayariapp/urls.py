from django.contrib import admin
from django.urls import path
from sayariapp import views
urlpatterns = [

   path('',views.sayariapp,name='hello'),
 path('scontect/',views.scontect,name='contect'),
   path('steam/', views.steam, name='team'),
    path('sad/', views.sad, name='sad'),
path('romantic/', views.romantic, name='romantic'),
   path('sabout/', views.sabout, name='about'),

path('sprofile/', views.sprofile, name='profile'),
    ]