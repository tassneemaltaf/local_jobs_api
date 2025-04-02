from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import JobListView, JobCreateView, JobAppListView, JobDeleteView
from .views import register, jobs_posted, apply

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('jobs_posted/', jobs_posted, name='jobs_posted'),
    path('', JobListView.as_view(), name='home'),
    path('new/', JobCreateView.as_view(), name='job_create'),
    path('job_apps/', JobAppListView.as_view(), name='job_apps'),
    path('apply/<int:pk>', apply, name='apply'),
    path('delete/<int:pk>/', JobDeleteView.as_view(), name='job_delete'),
]
