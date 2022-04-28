from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list_create), # 조회 # 작성    
    path('<int:notice_id>/', views.notice_update_delete), # 수정 # 삭제
]