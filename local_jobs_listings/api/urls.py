from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', Template_view.as_view(template_name='accounts/profile.html'), name='profile')
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home'),
]
