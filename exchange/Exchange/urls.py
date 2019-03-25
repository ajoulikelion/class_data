from django.contrib import admin
from django.urls import path
import rateapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('japan/',rateapp.views.japan, name = "japan"),
    path('china/',rateapp.views.china, name = "china"),
    path('usa/',rateapp.views.usa, name = "usa"),
    path('about/',rateapp.views.about, name="about"),
    path('result/',rateapp.views.result, name="result"),
   
]
