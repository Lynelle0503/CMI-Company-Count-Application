from django.db import models

# Create your models here.
class CompanyData(models.Model):
    name = models.CharField(max_length=100, default = '')
    domain = models.CharField(max_length=100, default = '')
    founded_year = models.CharField(max_length=10, default = '')
    industry = models.CharField(max_length=100, default = '')
    size_range =  models.CharField(max_length=20, default = '')
    locality = models.CharField(max_length=100, default = '')
    country = models.CharField(max_length=100, default = '')
    linkedin_url = models.CharField(max_length=100, default = '')
    curr_emp_estimate = models.CharField(max_length=20, default = '')
    total_emp_estimate =  models.CharField(max_length=20, default = '')
    
def __str__(self):
    return self.name
class CSVFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    