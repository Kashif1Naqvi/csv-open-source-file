from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class JobTitle(models.Model):
    job_title = models.CharField(max_length=250)


class Department(models.Model):
    department = models.CharField(max_length=250)
    
  
    

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    is_full_time = models.BooleanField(default=True)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.Name
    
    
    
    
    @property
    def full_part_titme(self):
        if(self.is_full_time):
            return True
        else:
            return False
        
    