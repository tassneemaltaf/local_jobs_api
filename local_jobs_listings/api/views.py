from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from .serializers import RegisterSerializer, JobSerializer
from django.http import Http404
from .models import Job, JobApplication

#Register a user function based view, it uses the CustomUserForm I created on forms.py
class RegisterAPIView(APIView):
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This List View is for all the jobs the applicant applied
class JobListAPIView(APIView):
  def get(self, request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

# Detail view for a single job
class JobDetailAPIView(APIView):
  def get_object(self, pk):
    try:
      return Job.objects.get(pk=pk)
    except Job.DoesNotExist:
      raise Http404

  def get(self, request, pk):
    job = self.get_object(pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)

#Applying for a job
class ApplyToJobAPI(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request, pk):
    try:
      job = Job.objects.get(pk=pk)

      if request.user.role != "job_seeker":
         return Response({"error": "Only job seekers can apply."}, status=403)

      # Check if already applied
      already_applied = JobApplication.objects.filter(job=job, applicant=request.user).exists()
      if already_applied:
        return Response({"detail": "You have already applied to this job."}, status=400)

      JobApplication.objects.create(job=job, applicant=request.user)
      return Response({"detail": "Application successful."}, status=201)

    except Job.DoesNotExist:
      return Response({"error": "Job not found."}, status=404)

#To see my applications for each applicant
class MyApplicationsAPI(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    applications = JobApplication.objects.filter(applicant=request.user)
    jobs = [app.job for app in applications]
    serialized_jobs = JobSerializer(jobs, many=True)
    return Response(serialized_jobs.data)

#Create a job only for recruiters
class JobCreateAPI(CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "recruiter":
            raise PermissionDenied("Only recruiters can create job posts.")
        serializer.save(recruiter=self.request.user)

#Check jobs I created, only for recruiters.
class MyJobPostsAPI(ListAPIView):
  serializer_class = JobSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    if self.request.user.role != "recruiter":
      return Job.objects.none()  
    return Job.objects.filter(recruiter=self.request.user)
  
class JobUpdateAPI(UpdateAPIView):
  serializer_class = JobSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    if self.request.user.role != "recruiter":
      raise PermissionDenied("Only recruiters can update job posts.")
    return Job.objects.filter(recruiter=self.request.user)

  def perform_update(self, serializer):
    job = self.get_object()
    if job.recruiter != self.request.user:
      raise PermissionDenied("You can only update your own job posts.")
    serializer.save()

class JobDeleteAPI(DestroyAPIView):
  queryset = Job.objects.all()
  permission_classes = [IsAuthenticated]

  def get_object(self):
    obj = super().get_object()
    if obj.recruiter != self.request.user:
      raise PermissionDenied("You can only delete your own job posts.")
    return obj