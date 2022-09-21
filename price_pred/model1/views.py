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
def index(request):
    if request.method == 'POST':
      if request.POST.get('ram')  :
        table=Data()
        table.Ram=request.POST.get('ram')
        table.Rom=request.POST.get('rom')
        table.mobile_size=request.POST.get('mob')
        table.Pri_cam=request.POST.get('pcam')
        table.sec_cam=request.POST.get('scam')
        table.battery=request.POST.get('battery')
        table.save() 
        messages.success(request,'Record saved')
        return redirect('index')
    return render(request,'index.html')
def __str__(self):
       return self.name

# def form(request):

#      open('./ml_model/refr.joblib','rb')
#      model=joblib.load('./ml_model/refr.joblib')
#      if request.method == 'POST':
#        if request.GET.get('ram')  :
#          dat=pre()
        
#          ram1=request.POST.get('ram')
#          rom1=request.POST.get('rom')
#          Pcam1=request.POST.get('pcam')
#          scam1=request.POST.get('scam')
#          battery=request.POST.get('battery')
#          mobi=request.POST.get('mob')
#          y_pred=model.predict(
#                 [['ram1','rom1','Pcam1','Pcam1','scam1','bat','bat1']]
#           )
         
#          dat.predict=y_pred
#          dat.save()
#          newval=y_pred
#          {'result':newval}
#          return redirect('/predict')
#      return render(request,predict)

       


# def prediction(request):
#    if request.method == 'POST':
#       if request.POST.get('predict')  :
#         ram1=request.GET('ram')
#         rom1=request.GET('rom')
#         Pcam1=request.GET('pcam')
#         scam1=request.GET('scam')
#         battery=request.GET('battery')
#         mobi=request.GET('mob')
#         y_pred=model.predict(
#                [[ram1,rom1,Pcam1,mobi,scam1,battery]]
#          )
         
#         dat=pre()
#         pre.predict=y_pred
#         pre.super().save() 
#         messages.success(request,'Record saved')
#         return redirect('/mod')
         
#    return render(request,'prediction.html') 
 
# @api_view(['GET'])
# def predict(request):
#     try:
#         request.method == 'POST'
#         ram = request.POST.get('ram')
#         rom = request.POST.get('rom')
#         pcam = request.POST.get('pcam')
#         scam = request.POST.get('scam')
#         battery = request.POST.get('battery')
#         mobs = request.POST.get('mob')
#         fields = [ram,rom,pcam,scam,battery,mobs]
        
#         if not None in fields:
#             #Datapreprocessing Convert the values to float
#             ram = float(ram)
#             rom = float(rom)
#             pcam= float(pcam)
#             scam = float(scam)
#             battery = float(battery)
#             mobs = float(mobs)
#             result = [ram,rom,pcam,scam,battery,mobs]
#             #[ram,rom,pcam,scam,battery,mobs]
#             #Passing data to model & loading the model from disks
#             model='./price_pred/ml_model/refr.joblib'
            
#             classi=joblib.load(open(model,'rb'))
      
#             prediction = classi.predict([result])
#             conf_score =  np.max(classi.predict_proba([result]))*100
           
#             predictions = {
                
#                 'error' : '0',
#                 'message' : 'Successfull',
#                 'prediction' : prediction,
#                 'confidence_score' : conf_score
#             }
#         else:
#             predictions = {
#                 'fieldserror':fields,
#                 'error' : '1',
#                 'message': 'Invalid Parameters'                
#             }
#     except Exception as e:
#         predictions = {
#             'error' : '2',
#             "message": str(e)
#         }
    
#     return Response(predictions)