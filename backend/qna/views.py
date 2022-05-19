from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from .serializers import QnaSerializer, ReviewSerializer
from .models import Qna, Review
# Create your views here.

###########
### QnA ###
###########
# @login_required
@api_view(['GET', 'POST'])
def qna_list_create(request):
    if request.method == 'GET':
        qna = Qna.objects.all()
        # qna = request.user.Qna_set.all()
        serializer = QnaSerializer(qna, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QnaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def qna_detail_update_delete(request, qna_id):
    qna = get_object_or_404(Qna, pk=qna_id)
    # if not request.user.qna_set.filter(pk=qna_id).exists():
    #     return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'GET':
        # qna = Qna.objects.all()
        # qna = request.user.qna_set.all()
        serializer = QnaSerializer(qna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QnaSerializer(qna, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        qna.delete()
        return Response({ 'id': qna_id }, status=status.HTTP_204_NO_CONTENT)

############
## Review ##
############

@api_view(['GET', 'POST'])
def review_list_create(request, qna_id):
    qna = Qna.objects.filter(pk=qna_id)[0]
    if request.method == 'GET':
        reviews = qna.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.data['qna'] = Qna.objects.filter(pk=qna_id)[0]
        # request.data['qna'] = qna_id
        serializer = ReviewSerializer(data=request.data)
        serializer.qna = qna
        print('one')
        print(serializer.qna)
        if serializer.is_valid(raise_exception=True):
            print('two')
            serializer.save(qna=qna)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_update_delete(request, qna_id, review_id):
    # qna = get_object_or_404(Qna, pk=qna_id)
    review = get_object_or_404(Review, pk=review_id)

    # if not request.user.review_set.filter(pk=review_id).exists():
    #     return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_id }, status=status.HTTP_204_NO_CONTENT)