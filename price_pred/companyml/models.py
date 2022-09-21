from django.db import models
import joblib
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier



# Create your models here.
class companyData(models.Model):
    ram=models.IntegerField()
    px_height=models.IntegerField()
    battery_pow=models.IntegerField()
    px_width=models.IntegerField()
    mobile_wt=models.IntegerField()
    int_mem=models.IntegerField()
    sc_h=models.IntegerField()
    talk_time=models.IntegerField()
    sc_w=models.IntegerField() 
    fc=models.IntegerField()
    n_core=models.IntegerField()
    pc=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    predictions=models.CharField(max_length=50,blank=True)
    class Meta:
     db_table='com_data'
    
     ordering=['-date']
    


    def save(self, *args, **kwargs):
      ml_model='./ml_model/class.joblib'
      classi=joblib.load(open(ml_model,'rb'))
      new=classi.predict(
         [[self.ram,self.px_height,self.battery_pow,self.px_width,self.mobile_wt,self.int_mem,self.sc_h,self.talk_time,self.sc_w,self.fc,self.n_core,
            self.pc]]  )
      X=float(new)      
      self.predictions=X
      

      return super().save(*args, *kwargs)



class Meta:
     db_table='com_data'
    
     ordering=['-date']
    
def __str__(self):
       return self.name

