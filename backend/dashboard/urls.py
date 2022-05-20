from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.temp_check), # 조회 # 작성    
    path('hourtemp/', views.hour_check)
]