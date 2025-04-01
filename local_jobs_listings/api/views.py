from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, JobApplication, CustomUser

def register(request):
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      redirect('login')
  else:
    form = CustomUserForm()
  return render(request, "api/register.html", {'form': form})


def jobs_posted(request):
  user = request.user
  if not user.is_authenticated:
    return render(request, "api/jobs_posted.html", {'jobs': [], 'user': user})
  
  jobs = Job.objects.filter(recruiter=user)
  return render(request, "api/jobs_posted.html", {'jobs': jobs, 'user': user})


# def apply(request):


class JobListView(generic.ListView):
  model = Job
  template_name = "api/job_list.html"
  context_object_name = 'jobs'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['user'] = self.request.user
    return context


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