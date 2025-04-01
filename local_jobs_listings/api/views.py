from django.shortcuts import render
from .forms import CustomUserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, JobApplication


class RegisterView(generic.CreateView):
  form_class = CustomUserForm
  success_url = reverse_lazy("login")
  template_name = "api/register.html"

class JobListView(generic.ListView):
  model = Job
  template_name = "api/job_list.html"
  context_object_name = 'jobs'


class JobCreateView(generic.CreateView, LoginRequiredMixin):
  model = Job
  fields = ['job_title', 'location', 'job_description']
  template_name = "api/job_create.html"
  context_object_name = 'jobs'
  success_url = reverse_lazy('home')

