from django.shortcuts import render, get_object_or_404
from .serializers import noticesSerializer
<<<<<<< HEAD
=======
from .models import notices
>>>>>>> develop
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def notice_list_create(request):
    # 조회
    if request.method == 'GET':
        notice = notices.objects.all()
        serializer = noticesSerializer(notice, many=True)
        return Response(serializer.data)
    # 작성
    elif request.method =='POST':
        serializer = noticesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response( serializer.data,status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
def notice_update_delete(request, notice_id):
    notice = get_object_or_404(notices, pk=notice_id)
    # 수정
    if request.method == 'PUT':
        serializer = noticesSerializer(notice, data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 삭제
    elif request.method == 'DELETE':
        notice.delete()
        return Response({'id':notice_id},status=status.HTTP_204_NO_CONTENT)
            