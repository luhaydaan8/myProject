from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Simple_jwt security features
# from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated



# Create your views here.

# Customer table api



'''
@api_view(['GET','POST'])
def get_and_post(request):
    if request.method == 'GET':
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def cusustomer_view(request,id):
    try:
        cust = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return Response({'message':'Id not exists!'})
    if request.method == 'GET':
        seralizer = CustomerSerializer(cust)
        return Response(seralizer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

        

    elif request.method == 'DELETE':
        cust.delete()
        return Response(f"Customer has been deleted")

'''


def generic_api(model_class, serializer_class):
    @api_view(['GET','POST', 'DELETE', 'PUT'])
    # @permission_classes([IsAuthenticated])


    def api(request, id = None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many = True)
                return Response(serializer.data)

        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Success
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # If serializer is invalid


        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    instance.delete()
                    return Response({'message':'Delete Successfully'})
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
                

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return Response(serializer.data)
                
                        
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    return api


manage_tool = generic_api(Tool, ToolSerializer)

manage_farmer = generic_api(Farmer, FarmerSerializer)

manage_loan = generic_api(Loan, LoanSerializer)

manage_maintenance = generic_api(Maintenance, MaintenanceSerializer)


#Login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # If authentication is successful, return a success response
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            else:
                # If authentication fails
                return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)