from rest_framework import serializers
from .models import Temp

class tempSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Temp
        fields = ('temp', 'message','created_at','hour')