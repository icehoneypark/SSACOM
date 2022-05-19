from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views



urlpatterns = [
    # jwt 유효토큰
    path('api-token-auth/', obtain_jwt_token),
    # 회원가입
    path('signup/', views.signup),
    # 유저 전체 조회
    path('username/', views.takeUsername),
    # 회원 탈퇴
    path('userdelete/<int:user_pk>/',views.userdelete),
    # 회원 정보 수정
    path('userchange/<int:user_pk>/',views.userchange),
    # 유정 정보 조회
    path('<int:user_pk>/', views.takeUser),
    
]
