from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class IndustryType(models.Model):
    industry_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.industry_name

class CompanyDetails(models.Model):
    industrytype = models.ForeignKey(IndustryType, on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=300)
    contact_regex = RegexValidator(regex=r'^\d{10}')
    contact_no = models.CharField(validators=[contact_regex], max_length=10, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name