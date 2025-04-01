from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, JobApplication

def register(request):
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
  else:
    form = CustomUserForm()
  return render(request, "api/register.html", {'form': form})


# class RegisterView(generic.CreateView):
#   form_class = CustomUserForm
#   success_url = reverse_lazy("login")
#   template_name = "api/register.html"

class JobListView(generic.ListView):
  model = Job
  template_name = "api/job_list.html"
  context_object_name = 'jobs'


class JobCreateView(LoginRequiredMixin, generic.CreateView):
  model = Job
  fields = ['job_title', 'location', 'job_description']
  template_name = "api/job_create.html"
  context_object_name = 'jobs'
  success_url = reverse_lazy('home')


class JobApplicationListView(generic.ListView):
  model = JobApplication
  template_name = "api/jobapplication_list.html"
  context_object_name = 'job_apps'