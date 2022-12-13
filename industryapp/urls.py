from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('storeIndustryType/', views.storeIndustryType, name='storeIndustryType'),
    path('editIndustryType/<str:pk>/', views.editIndustryType, name='editIndustryType'),
    path('storeCompanyDetails/', views.storeCompanyDetails, name='storeCompanyDetails'),
    path('editCompanyDetails/<str:pk>/', views.editCompanyDetails, name='editCompanyDetails'),
    path('deleteCompanyDetails/<str:pk>/', views.deleteCompanyDetails, name='deleteCompanyDetails'),
]