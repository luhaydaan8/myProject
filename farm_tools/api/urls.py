from myfarm_tools import views
from django.urls import path
from  myfarm_tools.views import LoginView


urlpatterns = [
    path('tools/', views.manage_tool),
    path('tools/<int:id>', views.manage_tool),

    path('farmers/', views.manage_farmer),
    path('farmers/<int:id>', views.manage_farmer),

    path('loans/', views.manage_loan),
    path('loans/<int:id>', views.manage_loan),

    path('maintenance/', views.manage_maintenance),
    path('maintenance/<int:id>', views.manage_maintenance),

    path('login/', LoginView.as_view(), name='login'),
]