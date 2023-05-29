from django.urls import path
from app_accounts.views import LoginView, DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
]