from rest_framework import serializers
from .models import faq

class faqSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = faq
        fields = ('id', 'title', 'content')
