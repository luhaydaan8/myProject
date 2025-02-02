# myfarm_tools/serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


# Tool Serializer
class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

# Farmer Serializer
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

# Loan Serializer
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

   
# Maintenance Serializer
class MaintenanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Maintenance
        fields = '__all__'

# Login Serialize
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)