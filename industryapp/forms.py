from django.forms import ModelForm
from .models import IndustryType, CompanyDetails

class IndustryTypeForm(ModelForm):
    class Meta():
        model = IndustryType
        fields = ['industry_name']

class CompanyDetailsForm(ModelForm):
    class Meta():
        model = CompanyDetails
        fields = '__all__'