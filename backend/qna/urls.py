from django.urls import path
from . import views


urlpatterns = [
    path('', views.qna_list_create), #qna 목록 조회(get), 생성(post)
    path('<int:qna_id>/', views.qna_detail_update_delete), #qna 상세조회(get), 수정(put), 삭제(delete)
    path('<int:qna_id>/review/', views.review_list_create), #review 목록 조회(get), 생성(post)
    path('<int:qna_id>/review/<int:review_id>/', views.review_update_delete), #review 수정(put), 삭제(delete)
]
