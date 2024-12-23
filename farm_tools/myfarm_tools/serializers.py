# myfarm_tools/serializers.py
from rest_framework import serializers
from .models import Tool, Farmer, Loan, Maintenance

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

# Loan Serializer
class LoanSerializer(serializers.ModelSerializer):
    tool = ToolSerializer()
    farmer = FarmerSerializer()

    class Meta:
        model = Loan
        fields = '__all__'

# Maintenance Serializer
class MaintenanceSerializer(serializers.ModelSerializer):
    tool = ToolSerializer()
    performed_by = FarmerSerializer()

    class Meta:
        model = Maintenance
        fields = '__all__'
