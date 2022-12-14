from django.shortcuts import render, get_object_or_404
from .serializers import faqSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def faq_list_create(request):
    # 조회
    if request.method == 'GET':
        faq = faq.objects.all()
        serializer = faqSerializer(faq, many=True)
        return Response(serializer.data)
    # 작성
    elif request.method =='POST':
        
        serializer = faqSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response( serializer.data,status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
def faq_update_delete(request, faq_id):
    faq = get_object_or_404(faq, pk=faq_id)
    # 수정
    if request.method == 'PUT':
        
        serializer = faqSerializer(faq, data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 삭제
    elif request.method == 'DELETE':
        faq.delete()
        return Response({'id':faq_id},status=status.HTTP_204_NO_CONTENT)
            