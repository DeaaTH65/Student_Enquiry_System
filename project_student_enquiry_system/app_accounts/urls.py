from django.urls import path
from app_accounts.views import LoginView, DashboardView, RegisterView, LogoutView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]