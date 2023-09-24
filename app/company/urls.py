"""
URL mappings for the user API.
"""
from django.urls import path

from company import views

app_name = 'company'

urlpatterns = [
    path('create/', views.CompanyView.as_view(), name='create'),
    path('owner_token/', views.CompanyView.as_view(), name='token'),
    path('owner/', views.ManageCompanyView.as_view(), name='owner'),
]
