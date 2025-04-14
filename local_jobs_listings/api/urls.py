from django.urls import path
from .views import JobListAPIView, JobDetailAPIView, RegisterAPIView, ApplyToJobAPI, MyApplicationsAPI, JobCreateAPI, MyJobPostsAPI, JobUpdateAPI, JobDeleteAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/jobs/', JobListAPIView.as_view(), name='api_job_list'),
    path('api/jobs/<int:pk>/', JobDetailAPIView.as_view(), name='api_job_detail'),
    path('jobs/<int:pk>/apply/', ApplyToJobAPI.as_view(), name='apply-to-job'),
    path('my-applications/', MyApplicationsAPI.as_view(), name='my-applications'),

    path('jobs/create/', JobCreateAPI.as_view(), name='job-update'),
    path('jobs/update/<int:pk>', JobUpdateAPI.as_view(), name='job-create'),
    path('jobs/delete/<int:pk>', JobDeleteAPI.as_view(), name='job-create'),
    path('my-jobs/', MyJobPostsAPI.as_view(), name='my-job-posts'),
]
