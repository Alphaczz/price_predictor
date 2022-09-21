from django.urls import path
from .import views
from django.contrib import admin
from django.urls import include
import model1

urlpatterns = [
    path('classi_ml',views.indexcom,name="indexcom"),                                                            
                                                                  
]
