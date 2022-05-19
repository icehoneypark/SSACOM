from rest_framework import serializers
from .models import temp

class tempSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = temp
        fields = ('temp', 'message', 'created_at')