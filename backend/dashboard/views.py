from django.shortcuts import render, get_object_or_404
from .serializers import tempSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def temp_check(request):
    # 조회
    if request.method == 'GET':
        temp = temp.objects.all()
        serializer = tempSerializer(temp, many=True)
        return Response(serializer.data)
    # 작성
    elif request.method =='POST':
        
        serializer = tempSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)