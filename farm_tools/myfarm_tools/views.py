from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Tool, Farmer, Loan, Maintenance
from .serializers import ToolSerializer, FarmerSerializer, LoanSerializer, MaintenanceSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Tool Views
class ToolListCreate(APIView):
    def get(self, request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToolDetail(APIView):
    def get(self, request, pk):
        try:
            tool = Tool.objects.get(pk=pk)
        except Tool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ToolSerializer(tool)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            tool = Tool.objects.get(pk=pk)
        except Tool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ToolSerializer(tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            tool = Tool.objects.get(pk=pk)
        except Tool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        tool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Farmer Views
class FarmerListCreate(APIView):
    def get(self, request):
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FarmerDetail(APIView):
    def get(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FarmerSerializer(farmer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        farmer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Loan Views
class LoanListCreate(APIView):
    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetail(APIView):
    def get(self, request, pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Maintenance Views
class MaintenanceListCreate(APIView):
    def get(self, request):
        maintenances = Maintenance.objects.all()
        serializer = MaintenanceSerializer(maintenances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceDetail(APIView):
    def get(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(maintenance)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        maintenance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Login (Obtain JWT Token) and Logout (Blacklist Token)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Login View - Generate access and refresh token
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]  # Anyone can access this view

# Logout View - Blacklist refresh token
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the token to revoke it
            return Response({"message": "Successfully logged out."}, status=200)
        except Exception as e:
            return Response({"message": str(e)}, status=400)
