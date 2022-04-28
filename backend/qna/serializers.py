from rest_framework import serializers
from .models import Qna, Review


class QnaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'content', 'category', 'created_at', 'updated_at')

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'qna', 'content', 'created_at', 'updated_at')
