from django.db import models

# Create your models here.
""""
comp_name,comp_type,comp_headq,how_old,comp_no_emp,comp_review,open_jobs,comp_services,comp_logo,comp_description

"""

class Types(models.Model):
   name = models.CharField(max_length=255, unique=True)
   
   def __str__(self):
      return self.name
   
   
class Company(models.Model):
   comp_name = models.CharField(max_length=255, unique=True)
   comp_type = models.ForeignKey(Types, on_delete=models.CASCADE)
   comp_headq= models.CharField(max_length=255)
   how_old= models.CharField(max_length=255)
   comp_no_emp = models.CharField(max_length=255)
   comp_review = models.CharField(max_length=255)
   open_jobs   = models.CharField(max_length=255)
   comp_services = models.CharField(max_length=255)
   comp_desc     = models.TextField()
   