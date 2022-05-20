from django.shortcuts import render, get_object_or_404
from .serializers import tempSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Temp
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def temp_check(request):
    # 조회
    if request.method == 'GET':
        temp = Temp.objects.all()
        serializer = tempSerializer(temp, many=True)
        return Response(serializer.data)
    # 작성
    elif request.method =='POST':
        
        serializer = tempSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET'])
@permission_classes([AllowAny])
def hour_check(request) :
    if request.method == 'GET' :
        temp = Temp.objects.filter(hour=1).order_by('-created_at')[:12]
        serializer = tempSerializer(temp, many=True)
        return Response(serializer.data)