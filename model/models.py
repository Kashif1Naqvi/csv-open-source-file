from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    full_or_part_time = models.CharField(max_length=1)
    salary_or_hourly = models.CharField(max_length=250)
    typical_hours = models.CharField(max_length=250)
    annual_salary = models.CharField(max_length=250)
    hourly_rate  = models.CharField(max_length=250)
    
    
    
    def __str__(self):
        return self.name
    
    
    
    