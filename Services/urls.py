from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_abandoned_individual, name='report_abandoned_individual'),
    path('report/success/', views.report_success, name='report_success'), 
    path('home/homenurse_reg/', views.homenurse_registration, name='homenurse_reg'),
    path('homenurse_reg/success/', views.registration_success, name='reg_success'),
    path('ambulance_service/', views.ambulance_service, name = 'ambulance_service'),
    path('ambulance_service/success/', views.ambulance_success, name = 'ambulance_success'),  
    path('feedback/', views.feedback, name = 'feedback'),
    path('activities/', views.Activities, name = 'activities'),
    path('inventory/',views.inventory,name='inventory')
]
