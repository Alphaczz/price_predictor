from django.shortcuts import render

# Create your views here.
from email import message
from msilib.schema import SelfReg
from joblib import load
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import *
from django. contrib import messages
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
import numpy as np

from sklearn.ensemble import RandomForestRegressor as rp

# Create your views here.


@csrf_exempt
def indexcom(request):
    if request.method == 'POST':
      if request.POST.get('ram')  :
        table=companyData()
        table.ram=request.POST.get('ram')
        table.px_height=request.POST.get('px_h')
        table.battery_pow=request.POST.get('batt_pow')
        table.px_width=request.POST.get('px_w')
        table.mobile_wt=request.POST.get('mob_weight')
        table.int_mem=request.POST.get('int_mem')
        table.sc_h=request.POST.get('sc_height')
        table.talk_time=request.POST.get('ttsc')
        table.sc_w=request.POST.get('s_width')
        table.fc=request.POST.get('front_c')
        table.n_core=request.POST.get('no_of_core')
        table.pc=request.POST.get('main_cam')
        table.save() 
        messages.success(request,'Record saved')
        return redirect('/index')
    return render(request,'classfication.html')

def __str__(self):
       return self.name