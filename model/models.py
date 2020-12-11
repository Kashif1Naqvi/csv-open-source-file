from django.db import models

# Create your models here.


# class JobTitle(models.Model):
#     job_title = models.CharField(max_length=250)

#     def __str__(self):
#         return self.JobTitle

# class Department(models.Model):
#     department = models.CharField(max_length=250)
    
#     def __str__(self):
#         return self.department
    
# class AnualSalary(models.Model):
#     anual_salary = models.CharField(max_length=250)
    

class Profile(models.Model):
    Name = models.CharField(max_length=250)
    JobTitle = models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    # full_or_part_time = models.CharField(max_length=1)
    AnnualSalary = models.CharField(max_length=250)
    # typical_hours = models.CharField(max_length=250)
    # annual_salary = models.CharField(max_length=250)
    # hourly_rate  = models.CharField(max_length=250)
    
    
    
    def __str__(self):
        return self.Name
    
    
    
    