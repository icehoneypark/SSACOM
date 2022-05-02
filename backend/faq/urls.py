from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list_create), # 조회 # 작성    
    path('<int:qna_id>/', views.faq_update_delete), # 수정 # 삭제
]