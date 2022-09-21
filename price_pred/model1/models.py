from django.db import models
import joblib
from sklearn.ensemble import RandomForestRegressor
import numpy as np




# Create your models here.
class Data(models.Model):
    Ram=models.IntegerField()
    Rom=models.IntegerField()
    mobile_size=models.IntegerField()
    Pri_cam=models.IntegerField()
    sec_cam=models.IntegerField()
    battery=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    predictions=models.CharField(max_length=50,blank=True)

    class pre(models.Model):
      predict= models.CharField(max_length=50,blank=True)
    def save(self, *args, **kwargs):
      ml_model='./ml_model/refr.joblib'
      classi=joblib.load(open(ml_model,'rb'))
      self.predictions=classi.predict(
         [[self.Ram,self.Rom,self.mobile_size,self.Pri_cam,self.sec_cam,self.battery]]
        )/10

      return super().save(*args, **kwargs)
    


    class Meta:
     db_table='model1_data'
    
     ordering=['-date']
    
    def __str__(self):
       return self.name

