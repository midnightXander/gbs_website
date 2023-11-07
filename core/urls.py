from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('astuces',views.astuces,name='astuces'),
    path('a propos',views.a_propos,name = 'a_propos')
    
]