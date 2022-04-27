from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer 
from .models import User

# 회원 가입
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# 유저 전체 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def takeUsername(request) : 
    if request.method == 'GET':
        user = get_user_model().objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)
# 유저 정보 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def takeUser(request, user_pk) :
    if request.method == 'GET' :
        user = User.objects.filter(id = user_pk)
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     if not username:
#         return Response({'Success':False,'error':'아이디를 입력해주세요.'},status=status.HTTP_200_OK)

#     if not get_user_model().objects.filter(username=username):
#         return Response({'Success':False,'error':'존재하지 않은 아이디입니다.'},status=status.HTTP_200_OK)

#     if not password:
#         return Response({'Success':False,'error':'비밀번호를 입력해주세요'},status=status.HTTP_200_OK)    
  
#     user = get_user_model().objects.get(username=username)
#     if not user.check_password(password):
#         return Response({'Success':False,'error':'비밀번호가 일치하지 않습니다.'},status=status.HTTP_200_OK)
   
#     return Response({'Success':True,'is_active':user.is_active},status=status.HTTP_200_OK)
# 회원 탈퇴
@api_view(['DELETE'])
@permission_classes([AllowAny])
def userdelete(request,user_pk):
    user = get_object_or_404(get_user_model(),pk=user_pk)
    if request.method =='DELETE':
        user.delete()
        data = {
            'delete': f'데이터 {user_pk}번이 삭제되없습니다.',
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
# 회원 정보 수정
@api_view(['PUT'])
@permission_classes([AllowAny])
def userchange(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'PUT' :
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)