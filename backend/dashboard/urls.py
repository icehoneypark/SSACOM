from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.temp_check), # ์กฐํ # ์์ฑ    
    path('hourtemp/', views.hour_check)
]