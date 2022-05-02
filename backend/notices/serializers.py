from rest_framework import serializers
from .models import notices

class noticesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = notices
        fields = ('id', 'title', 'content')