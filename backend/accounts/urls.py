from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views



urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('signup/', views.signup),
    path('username/', views.takeUsername),
    path('userdelete/<int:user_pk>/',views.userdelete),
    path('userchange/<int:user_pk>/',views.userchange),
    path('<int:user_pk>/', views.takeUser),
    
]
