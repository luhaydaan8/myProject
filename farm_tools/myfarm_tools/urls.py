from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, LogoutView, ToolListCreate, ToolDetail, FarmerListCreate, FarmerDetail, LoanListCreate, LoanDetail, MaintenanceListCreate, MaintenanceDetail

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenRefreshView.as_view(), name='token'), 

    # Other views for tools, farmers, loans, and maintenance
    path('tools/', ToolListCreate.as_view(), name='tool_list_create'),
    path('tools/<int:pk>/', ToolDetail.as_view(), name='tool_detail'),
    path('farmers/', FarmerListCreate.as_view(), name='farmer_list_create'),
    path('farmers/<int:pk>/', FarmerDetail.as_view(), name='farmer_detail'),
    path('loans/', LoanListCreate.as_view(), name='loan_list_create'),
    path('loans/<int:pk>/', LoanDetail.as_view(), name='loan_detail'),
    path('maintenances/', MaintenanceListCreate.as_view(), name='maintenance_list_create'),
    path('maintenances/<int:pk>/', MaintenanceDetail.as_view(), name='maintenance_detail'),
]
