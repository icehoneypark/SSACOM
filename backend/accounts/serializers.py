from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'

class UserChangeSerailizer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('phonenumber', 'fullname', 'email')