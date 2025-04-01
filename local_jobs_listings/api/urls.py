from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import JobListView, JobCreateView, JobApplicationListView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='api/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('', JobListView.as_view(), name='home'),
    path('new/', JobCreateView.as_view(), name='job_create'),
    path('job_apps/', JobApplicationListView.as_view(), name='job_apps'),
]
